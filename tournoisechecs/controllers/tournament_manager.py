from tournoisechecs.models.tournament import Tournament
from tournoisechecs.models.player import Player
from tournoisechecs.models.tournament import Tournament
from tournoisechecs.views.view_player import ViewPlayer
from tournoisechecs.views.view_tournament import ViewTournament
#from tournoisechecs.models.round import Round

NUMBER_TOURNAMENT_PLAYERS = 8

class TournamentManager:
    """Tournament controller"""

    def __init__(self):
        self.view_player = ViewPlayer()
        self.tournament_players = []
        self.view_tournament = ViewTournament()
        self.tournament = None


    def input_tournament_data(self):
        tournament_data = self.view_tournament.input_tournament_data()
        print(tournament_data)
        self.tournament = Tournament(tournament_data[0], tournament_data[1], tournament_data[2],
                                tournament_data[3], tournament_data[4], tournament_data[5])
        print()
        print(f"Vous avez créé un tournoi avec les informations suivantes :\n \n"
              f"Nom du tournoi : {self.tournament.tournament_name}\n"
              f"Lieu du tournoi : {self.tournament.place}\n"
              f"Date de début : {self.tournament.start_date}\n"
              f"Date de fin : {self.tournament.end_date}\n"
              f"Contrôle du temps : {self.tournament.time_control}\n"
              f"Description : {self.tournament.tournament_description}")
        print()
        return self.tournament

    def display_(self):
        self.view_tournament.display_tournament_data()

    def add_player(self):
        while len(self.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player_data = self.view_player.input_player_data()
            player = Player(player_data[0], player_data[1], player_data[2], player_data[3], player_data[4])
            self.tournament_players.append(player)
            print(self.tournament_players)

