from colorama import init, Back

from controllers.helpers import console_clear
from controllers.db_manager import TablePlayers, TableTournament
from views.view_menus import MenuMain

init()


def main():
    """
    - Uploads the players data from the file db.json with the class TablePlayer
    - Instantiates table_tournament to allow further upload of tournaments data from db.json
    - Opens the main menu with its choices of action
    """

    print(Back.BLACK)
    console_clear()
    print("Gestion des tournois d'échecs")
    console_clear(1)

    table_players = TablePlayers()
    table_players.install_players_data()

    table_tournament = TableTournament()

    init_menu = MenuMain()
    init_menu.main_choices(table_tournament)


if __name__ == "__main__":
    main()
