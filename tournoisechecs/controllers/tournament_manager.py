#from tournoisechecs.models.tournament import Tournament
from models.player import Player
#from tournoisechecs.models.round import Round

NUMBER_TOURNAMENT_PLAYERS = 8

class TournamentManager:
    """Tournament controller"""

    def __init__(self, view):
        self.view = view
        self.tournament_players = []

    def add_player(self):
        while len(self.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player_data = self.view.input_player_data()
            player = Player(player_data[0], player_data[1], player_data[2], player_data[3], player_data[4])
            self.tournament_players.append(player)
            print(self.tournament_players)

    def run(self):
        self.add_player()