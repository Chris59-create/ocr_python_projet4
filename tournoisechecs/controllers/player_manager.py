from models.player import Player
from views.view_player import ViewPlayer


class PlayerManager:

    view_player = ViewPlayer()
    players_instances = []

    def add_single_player(self):
        player_data = self.view_player.manual_input_player()
        player = Player(player_data["last_name"],
                        player_data["first_name"],
                        player_data["date_birth"],
                        player_data["gender"],
                        player_data["rank"]
                        )
        self.players_instances.append(player)

    # Ajoute la liste des joueurs au tournoi
    def tournament_add_players(self, tournament, NUMBER_TOURNAMENT_PLAYERS):
        while len(tournament.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player_data = self.view_player.input_player_data()
            player = Player(player_data["last_name"],
                            player_data["first_name"],
                            player_data["date_birth"],
                            player_data["gender"],
                            player_data["rank"]
                            )
            self.players_instances.append(player)
            tournament.tournament_players.append(player)

    def test_tournament_add_players(self, tournament, NUMBER_TOURNAMENT_PLAYERS):
        while len(tournament.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player_data = self.view_player.random_input_player()
            player = Player(player_data["last_name"],
                            player_data["first_name"],
                            player_data["date_birth"],
                            player_data["gender"],
                            player_data["rank"]
                            )
            self.players_instances.append(player)
            tournament.tournament_players.append(player)
        print("\nJoueurs ajoutés au tournoi\n")
        print(tournament.tournament_players)

    def update_player_rank(self):
        self.view_player.display_all_players_by_name(self.players_instances)
        player_id, new_rank = self.view_player.input_player_new_rank()
        for player in self.players_instances:
            if player.player_id == player_id:
                player.change_rank(new_rank)
