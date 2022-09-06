from controllers.db_manager import TablePlayers
from views.view_menus import MenuMain
from views.view_test import  PlayersListTest


def main():

    # install data from db.json
    table_players = TablePlayers()
    table_players.install_players_data()

    # test à supprimer liste players
    player_list_test = PlayersListTest()

    # Launch the main menu
    init_menu = MenuMain()
    init_menu.main_choices()


if __name__ == "__main__":
    main()
