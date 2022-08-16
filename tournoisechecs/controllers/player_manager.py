from tinydb import TinyDB
from datetime import datetime
from models.player import Player
from views.view_player import ViewPlayer

db = TinyDB('db.json')
players_table = db.table("players")


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

    def save_players_data(self):

        players_table.truncate()

        serialized_players = []
        for player in Player.players_instances:
            date_birth_str = player.date_birth.strftime('%d%m%Y')
            serialized_player = {
                'last_name': player.last_name,
                'first_name': player.first_name,
                'date_birth': date_birth_str,
                'gender': player.gender,
                'rank': player.rank,
                'current_tournament_score': player.current_tournament_score,
                'player_id': player.player_id
            }
            serialized_players.append(serialized_player)

        players_table.insert_multiple(serialized_players)

    def install_players_data(self):

        serialized_players = players_table.all()
        for deserialized_player in serialized_players:
            date_birth = datetime.strptime(deserialized_player['date_birth'], '%d%m%Y')
            player = Player(deserialized_player['last_name'],
                            deserialized_player['first_name'],
                            date_birth,
                            deserialized_player['gender'],
                            deserialized_player['rank'],
                            deserialized_player['current_tournament_score'],
                            deserialized_player['player_id'])