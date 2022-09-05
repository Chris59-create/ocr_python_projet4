from controllers.player_manager import PlayerManager
from controllers.swisspairs_manager import SwissPairs
from models.match import Match
from models.round import Round
from models.tournament import Tournament
from views.view_round import ViewRound
from views.view_tournament import ViewTournament

NUMBER_TOURNAMENT_PLAYERS = 8
NUMBER_ROUNDS = 4


class TournamentManager:
    """Tournament controller"""

    tournaments_instances = []
    number_rounds = 1

    def __init__(self):
        self.view_tournament = ViewTournament()

    # Crée le tournoi
    def input_tournament_data(self):
        tournament_data = self.view_tournament.input_tournament_data()  # à rétablir pour prod
        # tournament_data = self.view_tournament.input_tournament_data()  # test à supprimer pour prod
        self.tournament = Tournament(tournament_data["tournament_name"],
                                     tournament_data["place"],
                                     tournament_data["dates_tournament"],
                                     tournament_data["time_control"],
                                     tournament_data["tournament_description"]
                                     )
        self.tournaments_instances.append(self.tournament)

    # Affiche les infos du tournoi
    def display_tournament_data(self):
        # view_tournament = ViewTournament()
        self.view_tournament.display_tournament_data(self.tournament)

    # Ajoute la liste des joueurs au tournoi
    def tournament_add_players(self):
        player_manager = PlayerManager()
        while len(self.tournament.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player = player_manager.add_player()
            self.tournament.tournament_players.append(player)

    # Calcule les paires de joueurs pour le round
    def calculate_pairs(self):
        pairs = SwissPairs()
        pairs_players = pairs.run_creation_pairs_players(self.tournament.tournament_players,
                                                         self.tournament.tournament_rounds, self.number_rounds)
        print("test pairs_players after swisspairs : ", pairs_players)
        return pairs_players

    def prepare_round(self):
        round_name = "Round " + str(self.number_rounds)
        print(round_name)  # test à supprimer

        pairs_players = self.calculate_pairs()
        view_round = ViewRound()
        view_round.display_pairs_round(pairs_players)

        self.number_rounds += 1

        return round_name, pairs_players

    def start_round(self, round_name, pairs_players):
        self.round_ = Round(round_name, pairs_players)
        print(f"Date et heure du début de {round_name} : {self.round_.start_date_time}")

    def update_score(self):
        view_round = ViewRound()
        self.round_.end_round()
        for pair_players in self.round_.pairs_players:
            player1 = pair_players[0]
            player2 = pair_players[1]
            score_player1, score_player2 = view_round.input_score(player1, player2)
            match = Match(player1, score_player1, player2, score_player2)

            player1.update_current_tournament_score(score_player1)
            player2.update_current_tournament_score(score_player2)

            self.round_.add_match(match.match_tuple)

        self.tournament.add_round(self.round_)

    def update_tournament_final_scores(self):
        self.remaining_rounds = NUMBER_ROUNDS - len(self.tournament.tournament_rounds)
        # ! Check if all rounds have been played before updating the tournament final scores
        if self.remaining_rounds == 0:
            for player in self.tournament.tournament_players:
                final_tournament_score = [player, player.current_tournament_score]
                self.tournament.tournament_final_scores.append(final_tournament_score)
                player.current_tournament_score = 0
        else:
            # view_tournament = ViewTournament()
            self.view_tournament.display_tournament_in_progress()
            # back to the menu

    def player_data(self, element, index_element):
        tournament_rank = index_element
        first_name = element[0].first_name
        last_name = element[0].last_name
        date_birth = element[0].date_birth
        rank = element[0].rank
        score = element[1]

        player_data = {"tournament_rank": tournament_rank,
                       "first_name": first_name,
                       "last_name": last_name,
                       "date_birth": date_birth,
                       "rank": rank,
                       "score": score
                       }

        return player_data

    def display_tournament_total_scores(self):

        self.view_tournament.display_remaining_rounds(self.remaining_rounds)
        self.tournament_final_scores_sorted = sorted(self.tournament.tournament_final_scores, key=lambda x: x[1],
                                                     reverse=True)
        for element in self.tournament_final_scores_sorted:
            index_element = self.tournament_final_scores_sorted.index(element)
            player_data = self.player_data(element, index_element)
            self.view_tournament.display_tournament_total_scores(player_data)

        print()

    def update_tournament_players_ranks(self):

        self.display_tournament_total_scores()
        print("test affichage individuel des joueurs pour maj rank")
        for element in self.tournament_final_scores_sorted:
            index_element = self.tournament_final_scores_sorted.index(element)
            player_data = self.player_data(element, index_element)
            self.view_tournament.display_tournament_total_scores(player_data)
            new_rank = self.view_tournament.input_tournament_player_new_rank()
            element[0].rank = new_rank
