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
        tournament_data = view_tournament.input_tournament_data()
        self.tournament = Tournament(tournament_data[0], tournament_data[1], tournament_data[2],
                                tournament_data[3], tournament_data[4])

        return self.tournament

    # Affiche les infos du tournoi
    def display_tournament_data(self):
        #view_tournament = ViewTournament()
            self.view_tournament.display_tournament_data(self.tournament)

    # Ajoute la liste des joueurs au tournoi
    def add_players(self):
        view_player = ViewPlayer()
        while len(self.tournament.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player_data = view_player.input_player_data()
            player = Player(player_data[0], player_data[1], player_data[2], player_data[3], player_data[4])
            self.tournament.tournament_players.append(player)

        return self.tournament.tournament_players

    def test_add_players(self):
        view_player = ViewPlayer()
        while len(self.tournament.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player_data = view_player.random_input_player()
            player = Player(player_data[0], player_data[1], player_data[2], player_data[3], player_data[4])
            self.tournament.tournament_players.append(player)

        return self.tournament.tournament_players

    # Calcule les paires de joueurs pour le round
    def calculate_pairs(self):
        pairs = SwissPairs()
        pairs_players = pairs.run_creation_pairs_players(self.tournament.tournament_players,
                                                         self.tournament.tournament_rounds, self.number_rounds)
        return pairs_players

    def prepare_round(self):
        self.round_name = "Round " + str(self.number_rounds)
        print(self.round_name) # test à supprimer
      
        self.pairs_players = self.calculate_pairs()
        view_round = ViewRound()
        view_round.display_pairs_round(self.pairs_players)

        self.number_rounds += 1
        
        return self.round_name, self.pairs_players
        
    def start_round(self):
        self.round_  = Round(self.round_name, self.pairs_players)
        print(self.round_.start_date_time)

    def update_score(self):
        view_round = ViewRound()
        for pair_players in self.round_.pairs_players:
            player1 = pair_players[0]
            player2 = pair_players[1]
            score_player1, score_player2 = view_round.input_score(player1, player2 )
            match = Match(player1, score_player1, player2, score_player2)

            player1.update_current_tournament_score(score_player1)
            player2.update_current_tournament_score(score_player2)

            print(f"\ntotal score {player1.last_name} : {player1.current_tournament_score}\n"
                  f"total score {player2.last_name} : {player2.current_tournament_score}\n")

            self.round_.add_match(match.match_tuple)
        print("les matches joués dans le round : ", self.round_.matches) #à supprimer

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
        print("Number rounds : ", NUMBER_ROUNDS) #à supprimer
        print("nombre de rounds : ",  len(self.tournament.tournament_rounds)) # à supprimer
        print("nom du tournoi : ", self.tournament.tournament_name) # à supprimer
        stop = input("pause to check the process : ") #à supprimer
        remaining_rounds = NUMBER_ROUNDS - len(self.tournament.tournament_rounds)
        #view_tournament = ViewTournament() # à vérifier si nécessaire
        self.view_tournament.display_tournament_total_scores(remaining_rounds)




    # Met à jour les scores des matchs de la tournée
    # Ajoute les matchs à la tournée
    # Totalise les scores de chaque joueur du tournoi
# Calcule les paires de joueurs pour tournée suivante restante
    # idem chaque tournée

# Affiche les scores du tournoi

    def run_tournament_manager(self):
        self.input_tournament_data()
        self.display_tournament_data()
        self.add_players()
        self.prepare_round(NUMBER_ROUNDS)
        self.start_round()
        self.round_.end_round()

    def run_tournament_test(self):
        self.tournament = Tournament("tournoi test", "Villeneuve d'Ascq", ['22/07/2022', '30/07/2022'], "Bullet",
                                     "Ce sont des informations statiques")
        self.display_tournament_data()
        self.test_add_players()
        i = 0
        while i < NUMBER_ROUNDS:
            print("\nstart prepare_round\n")
            self.prepare_round()
            print("\nend prepare_round\n")
            print("\nstart start_round\n")
            self.start_round()
            print("\nend start_round\n")
            print("\nstart end_round\n")
            self.round_.end_round()
            print("\nend end_round\n")
            print(self.round_.end_date_time)
            print("\nstart update_score\n")
            self.update_score()
            print("\nend update_score\n")
            print("test nombre de matchs dans le tour : ", len(self.round_.matches))
            print("\nstart tournament.add_round\n")
            self.tournament.add_round(self.round_)
            print("\nend tournament.add_round\n")
            print()
            i += 1
        self.update_tournament_final_scores()
        print("start display_tournament_total_score")
        self.display_tournament_total_scores()
        print()




        

