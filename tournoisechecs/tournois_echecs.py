from views.view_menus import MenuMain
from controllers.player_manager import PlayerManager


def main():

    # install data from db.json
    player_manager = PlayerManager()
    player_manager.install_players_data()


    # Launch the main menu
    init_menu = MenuMain()
    init_menu.main_choices()

if __name__ == "__main__":
    main()