from tinydb import TinyDB
from datetime import datetime
from models.player import Player
from views.view_player import ViewPlayer

db = TinyDB('db.json')
players_table = db.table("players")


class PlayerManager:

    view_player = ViewPlayer()
    players_instances = []

    def add_single_player(self):
        player_data = self.view_player.manual_input_player()
        player = Player(player_data["last_name"],
                        player_data["first_name"],
                        player_data["date_birth"],
                        player_data["gender"],
                        player_data["rank"])
        self.players_instances.append(player)

    # Ajoute la liste des joueurs au tournoi
    def tournament_add_players(self, tournament, NUMBER_TOURNAMENT_PLAYERS):
        while len(tournament.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player_data = view_player.input_player_data()
            player = Player(player_data["last_name"],
                            player_data["first_name"],
                            player_data["date_birth"],
                            player_data["gender"],
                            player_data["rank"])
            self.players_instances.append(player)
            tournament.tournament_players.append(player)

    def test_tournament_add_players(self, tournament, NUMBER_TOURNAMENT_PLAYERS):
        while len(tournament.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player_data = self.view_player.random_input_player()
            player = Player(player_data["last_name"],
                            player_data["first_name"],
                            player_data["date_birth"],
                            player_data["gender"],
                            player_data["rank"])
            self.players_instances.append(player)
            tournament.tournament_players.append(player)
        print("\nJoueurs ajoutés au tournoi\n")



    def update_player_rank(self):
        self.view_player.display_all_players_by_name(self.players_instances)
        player_id, new_rank = self.view_player.input_player_new_rank()
        print(player_id) # à supprimer
        print(new_rank) # à supprimer
        for player in self.players_instances:
            if player.player_id == player_id:
                player.change_rank(new_rank)

    def save_players_data(self):

        players_table.truncate()

        serialized_players = []
        for player in self.players_instances:
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

        deserialized_players = players_table.all()
        for deserialized_player in deserialized_players:
            date_birth = datetime.strptime(deserialized_player['date_birth'], '%d%m%Y')
            player = Player(deserialized_player['last_name'],
                            deserialized_player['first_name'],
                            date_birth,
                            deserialized_player['gender'],
                            deserialized_player['rank'],
                            deserialized_player['current_tournament_score'],
                            deserialized_player['player_id'])
            self.players_instances.append(player)