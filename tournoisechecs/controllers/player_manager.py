from models.player import Player
from views.view_player import ViewPlayer


class PlayerManager:
    """
    Contains the methods needed to manage the players.
    Class variables:
    - players_instances: an empty list to store the future players
    - view_player:  instance of ViewPlayer to allow further use of
                    methods to input or display players data.
    """

    players_instances = []
    view_player = ViewPlayer(players_instances)

    def add_player(self):
        """Called by method of TournamentManager (module tournament_manager
        in controllers) and by MenuPlayer (module view_menus in views.
        Calls the method needed to select a player or collect the data for
        a new player. Returns None to end the action if the user has chosen
        to cancel, a player if found in existing list, if not create a
        new player object of the class Player (module player in models)
        and returns this player."
        """

        player_data = self.view_player.player_selection(player_selection_data={},
                                                        players_list=self.players_instances,
                                                        i=0
                                                        )

        if not player_data:

            return None

        else:

            if isinstance(player_data, Player):
                return player_data

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
        """Calls the method to find a player and if found or created
        calls the method to input a new rank and use it to update the
        player rank."""

        player = self.add_player()

        if player:

            new_rank = self.view_player.input_player_new_rank()
            player.change_rank(new_rank)

        else:

            return

    def display_players(self, players_list, criteria):
        """According to the criteria passed in the method, sorts the
        players_list and passes the sorted list and the criteria to
        the method which will display the sorted list."""

        players_sorted = []

        if criteria == "alphabetical":
            players_sorted = sorted(players_list, key=lambda x: (x.last_name, x.first_name))

        elif criteria == "rank":
            players_sorted = sorted(players_list, key=lambda x: (x.rank, x.last_name, x.first_name))

        self.view_player.display_players(players_sorted, criteria)
