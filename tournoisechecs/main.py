#from controllers.tournament_manager import TournamentManager
from views.view_menus import MenuMain




def main():
    # init_tournament = TournamentManager()
    #init_tournament.run_tournament_test()

    init_menu = MenuMain()
    init_menu.choices()




if __name__ == "__main__":
    main()