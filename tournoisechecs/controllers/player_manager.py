from models.player import Player
from views.view_player import ViewPlayer


class PlayerManager:

    view_player = ViewPlayer()

    def add_single_player(self):
        player_data = self.view_player.manual_input_player()
        player = Player(player_data[0], player_data[1], player_data[2], player_data[3], player_data[4])

    def display_all_players(self):
        for player in Player.players_instances:
            print(player)

    def display_all_players_by_name(self):
        all_players_by_rank = sorted(Player.players_instances, key=lambda x: (x.first_name, x.last_name))
        for player in all_players_by_rank:
            print(player)


    def update_player_rank(self):
        self.display_all_players()
        player_id, new_rank = self.view_player.input_player_new_rank()
        print(player_id) # à supprimer
        print(new_rank) # à supprimer
        for player in Player.players_instances:
            if player.player_id == player_id:
                player.change_rank(new_rank)
            else:
                print("Aucun joueur avec cet ID dans la liste des joueurs !\nVérifier l'ID et recommencer la saisie.")
                break