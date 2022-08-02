from models.player import Player
from models.tournament import Tournament
from models.tournament import TournamentScore
from models.round import Round
from models.match import Match
from controllers.swisspairs_manager import SwissPairs
from views.view_player import ViewPlayer
from views.view_tournament import ViewTournament
from views.view_round import ViewRound

#from models.round import Round

NUMBER_TOURNAMENT_PLAYERS = 8
NUMBER_ROUNDS = 4


class TournamentManager:
    """Tournament controller"""

    number_rounds = 1

    # Crée le tournoi
    def input_tournament_data(self):
        view_tournament = ViewTournament()
        tournament_data = view_tournament.input_tournament_data()
        self.tournament = Tournament(tournament_data[0], tournament_data[1], tournament_data[2],
                                tournament_data[3], tournament_data[4])

        return self.tournament

    # Affiche les infos du tournoi
    def display_tournament_data(self):
        view_tournament = ViewTournament()
        view_tournament.display_tournament_data(self.tournament)

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
        pairs_players = pairs.run_creation_pairs_players(self.tournament.tournament_players)
        return pairs_players

    def prepare_round(self):
        self.round_name = "Round " + str(self.number_rounds)
        print(self.round_name) # test à supprimer
      
        self.pairs_players = self.calculate_pairs()
        view_round = ViewRound()
        view_round.display_pairs_round(self.pairs_players)

        #self.number_rounds += 1 à supprimer après vérification
        
        return self.round_name, self.pairs_players
        
    def start_round(self):
        self.round_  = Round(self.round_name, self.pairs_players)
        print(self.round_.start_date_time)

    def update_score(self):
        view_round = ViewRound()
        for pair_players in self.round_.pairs_players:
            score_joueur1, score_joueur2 = view_round.input_score(pair_players[0], pair_players[1])
            match = Match(pair_players[0], score_joueur1, pair_players[1], score_joueur2)

            tournament_score1 = TournamentScore(pair_players[0], score_joueur1)
            tournament_score1.totalize_score()
            tournament_score2 = TournamentScore(pair_players[1], score_joueur2)
            tournament_score2.totalize_score()


            self.round_.add_match(match.match_tuple)
        print(self.round_.matches)



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
        i=0
        while i < NUMBER_ROUNDS:
            self.prepare_round()
            self.start_round()
            self.round_.end_round()
            print(self.round_.end_date_time)
            self.update_score()
            print("test nombre de matchs dans le tour : ", len(self.round_.matches))
            self.tournament.add_round(self.round_)
            print()
            i += 1


        

