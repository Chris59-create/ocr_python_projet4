import pyinputplus as pyip
from views.menu_tournament import MenuTournament
from views.menu_players import MenuPlayers
from views.menu_reports import MenuReports

manage_tournament = None

class MenuMain:

    def __init__(self):
        print("Nenu principal\n")

    def manage_tournament(self):

        global manage_tournament

        if isinstance(manage_tournament, MenuTournament):
            manage_tournament.choices()
        else:
            manage_tournament = MenuTournament()
            manage_tournament.choices()

    def manage_players(self):
        MenuPlayers()

    def edit_reports(self):
        MenuReports()

    def choices(self):
        main_choice = pyip.inputMenu(["Gérer un tournoi", "Gérer les joueurs", "Editer les rapports"],
                                     prompt="Saisir le chiffre de l'action désirée :\n", numbered=True)
        if main_choice == "Gérer un tournoi":
            self.manage_tournament()
        if main_choice == "Gérer les joueurs":
            self.manage_players()
        if main_choice == "Editer les rapports":
            self.edit_reports()
