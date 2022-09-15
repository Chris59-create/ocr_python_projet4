from controllers.helpers import console_clear
from controllers.db_manager import TablePlayers, TableTournament
from views.view_menus import MenuMain


def main():
    """ - Downloads the players data from the file db.json and use them
     to instantiate the relative objets
    - Open the main menu to allow to choice desired action"""

    console_clear()
    print("Gestion des tournois d'échecs")
    console_clear(2)

    # install data from db.json
    table_players = TablePlayers()
    table_players.install_players_data()

    # instantiate the class which manages to backup and and recovery of tournaments data
    table_tournament = TableTournament()

    # Launch the main menu
    init_menu = MenuMain()
    init_menu.main_choices(table_tournament)


if __name__ == "__main__":
    main()
