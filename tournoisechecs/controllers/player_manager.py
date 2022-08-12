from models.player import Player
from views.view_player import ViewPlayer

class PlayerManager:

    view_player = ViewPlayer()
    player = Player()

    def add_player(self):
        player_data = self.view_player.input_player_data()
        player = Player(player_data[0], player_data[1], player_data[2], player_data[3], player_data[4])

    def update_player_rank(self):
        #player_id, new_rank = self.view_player.input_player_new_rank()
        #self.player.change_rank(player_id, new_rank)
        pass