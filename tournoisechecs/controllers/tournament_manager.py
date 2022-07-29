#from tournoisechecs.models.tournament import Tournament
from models.player import Player
#from tournoisechecs.models.round import Round

NUMBER_TOURNAMENT_PLAYERS = 1

class TournamentManager:
    """Tournament controller"""

    def __init__(self, view):
        self.view = view
        self.tournament_players = []

    def manual_add_player(self):
        while len(self.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player_data = self.view.input_player_data_manual()
            player = Player(player_data[0], player_data[1], player_data[2], player_data[3], player_data[4])
            self.tournament_players.append(player)
            print(self.tournament_players)

    def from_dataset_add_player(self):
        pass

    def run_test(self):
        input_mode = "manual"
        if input_mode == "manual":
            self.manual_add_player()
        else:
            self.from_dataset_add_player()