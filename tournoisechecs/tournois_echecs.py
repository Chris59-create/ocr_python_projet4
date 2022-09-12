from controllers.db_manager import TablePlayers
from views.view_menus import MenuMain


def main():
    """ - Downloads the players data from the file db.json and use them
     to instantiate the relative objets
    - Open the main menu to allow to choice desired action"""

    # install data from db.json
    table_players = TablePlayers()
    table_players.install_players_data()

    # Launch the main menu
    init_menu = MenuMain()
    init_menu.main_choices()


if __name__ == "__main__":
    main()
