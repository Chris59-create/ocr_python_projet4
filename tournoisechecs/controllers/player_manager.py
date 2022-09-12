from models.player import Player
from views.view_player import ViewPlayer


class PlayerManager:

    players_instances = []
    view_player = ViewPlayer(players_instances)

    def add_player(self):
        player_data = self.view_player.player_selection(player_selection_data={},
                                                        players_list=self.players_instances,
                                                        i=0
                                                        )

        if isinstance(player_data, Player):
            player = player_data

        else:
            player = Player(player_data["last_name"],
                            player_data["first_name"],
                            player_data["date_birth"],
                            player_data["gender"],
                            player_data["rank"]
                            )
            self.players_instances.append(player)

        return player

    def update_player_rank(self):
        player = self.view_player.player_selection(player_selection_data={},
                                                   players_list=self.players_instances,
                                                   i=0
                                                   )
        new_rank = self.view_player.input_player_new_rank()
        player.change_rank(new_rank)

    def display_players(self, players_list, criteria):

        players_sorted = []

        if criteria == "alphabetical":
            players_sorted = sorted(players_list, key=lambda x: (x.last_name, x.first_name))

        elif criteria == "rank":
            players_sorted = sorted(players_list, key=lambda x: (x.rank, x.last_name, x.first_name))

        self.view_player.display_players(players_sorted, criteria)
