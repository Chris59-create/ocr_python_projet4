#from controllers.tournament_manager import TournamentManager
from views.view_menus import MenuMain




def main():

    # install data from db.json


    # Launch the main menu
    init_menu = MenuMain()
    init_menu.main_choices()

if __name__ == "__main__":
    main()