from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from controllers.swisspairs_manager import SwissPairs
from views.view_player import ViewPlayer
from views.view_tournament import ViewTournament
from views.view_round import ViewRound

NUMBER_TOURNAMENT_PLAYERS = 8
NUMBER_ROUNDS = 4 # à récupérer dans le model Tournament ou à supprimer dans ce dernier


class TournamentManager:
    """Tournament controller"""

    number_rounds = 1

    def __init__(self):
        self.view_tournament = ViewTournament()

    # Crée le tournoi
    def input_tournament_data(self):
        #self.view_tournament = ViewTournament()
        #tournament_data = self.view_tournament.input_tournament_data() #à rétablir pour prod
        tournament_data = self.view_tournament.test_tournament_data() # test à supprimer pour prod
        self.tournament = Tournament(tournament_data[0], tournament_data[1], tournament_data[2],
                                tournament_data[3], tournament_data[4])

    # Affiche les infos du tournoi
    def display_tournament_data(self):
        #view_tournament = ViewTournament()
            self.view_tournament.display_tournament_data(self.tournament)

    # Ajoute la liste des joueurs au tournoi
    def tournament_add_players(self):
        view_player = ViewPlayer()
        while len(self.tournament.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player_data = view_player.input_player_data()
            player = Player(player_data[0], player_data[1], player_data[2], player_data[3], player_data[4])
            self.tournament.tournament_players.append(player)

    def test_tournament_add_players(self):
        view_player = ViewPlayer()
        while len(self.tournament.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player_data = view_player.random_input_player()
            player = Player(player_data[0], player_data[1], player_data[2], player_data[3], player_data[4])
            self.tournament.tournament_players.append(player)
        print("\nJoueurs ajoutés au tournoi\n")

    # Calcule les paires de joueurs pour le round
    def calculate_pairs(self):
        pairs = SwissPairs()
        pairs_players = pairs.run_creation_pairs_players(self.tournament.tournament_players,
                                                         self.tournament.tournament_rounds, self.number_rounds)
        return pairs_players

    def prepare_round(self):
        round_name = "Round " + str(self.number_rounds)
        print(round_name) # test à supprimer
      
        pairs_players = self.calculate_pairs()
        view_round = ViewRound()
        view_round.display_pairs_round(pairs_players)

        self.number_rounds += 1
        
        return round_name, pairs_players
        
    def start_round(self, round_name, pairs_players ):
        round_ = Round(round_name, pairs_players)
        print(f"Date et heure du début de {round_name} : {round_.start_date_time}")

        return round_

    def update_score(self, round_):
        view_round = ViewRound()
        for pair_players in round_.pairs_players:
            player1 = pair_players[0]
            player2 = pair_players[1]
            score_player1, score_player2 = view_round.input_score(player1, player2 )
            match = Match(player1, score_player1, player2, score_player2)

            player1.update_current_tournament_score(score_player1)
            player2.update_current_tournament_score(score_player2)

            round_.add_match(match.match_tuple)

        self.tournament.add_round(round_)

    def update_tournament_final_scores(self):
        remaining_rounds = NUMBER_ROUNDS - len(self.tournament.tournament_rounds)
        # ! Check if all rounds have been played before updating the tournament final scores
        if remaining_rounds == 0:
            for player in self.tournament.tournament_players:
                final_tournament_score = [player, player.current_tournament_score]
                self.tournament.tournament_final_scores.append(final_tournament_score)
                player.current_tournament_score = 0
        else:
            #view_tournament = ViewTournament()
            self.view_tournament.display_tournament_in_progress(remaining_rounds)
            # back to the menu

    def display_tournament_total_scores(self):
        remaining_rounds = NUMBER_ROUNDS - len(self.tournament.tournament_rounds)
        self.view_tournament.display_tournament_total_scores(remaining_rounds)

    def update_tournament_players_ranks(self):
        view_player = ViewPlayer()
        self.display_tournament_total_scores()
        tournament_final_scores_sorted = sorted(self.tournament.tournament_final_scores, key=lambda x: x[1],
                                                reverse=True)
        for element in tournament_final_scores_sorted:
            print()
            print(f"{tournament_final_scores_sorted.index(element)+1}. {element[0].first_name} "
                  f"{element[0].last_name} (ID {element[0].player_id}) - Classement : {element[0].rank} - Score :"
                  f" {element[1]} ;")
            new_rank = self.view_tournament.input_tournament_player_new_rank()
            element[0].rank = new_rank





        

