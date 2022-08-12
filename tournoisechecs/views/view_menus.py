import pyinputplus as pyip
import sys
from controllers.tournament_manager import TournamentManager, NUMBER_ROUNDS

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
        main_choice = pyip.inputMenu(["Gérer un tournoi", "Gérer les joueurs", "Editer les rapports",
                                      "Quitter l'application"],
                                     prompt="Saisir le chiffre de l'action désirée :\n", numbered=True)
        if main_choice == "Gérer un tournoi":
            self.manage_tournament()
        if main_choice == "Gérer les joueurs":
            self.manage_players()
        if main_choice == "Editer les rapports":
            self.edit_reports()
        if main_choice == "Quitter l'application":
            sys.exit("Application fermée par l'utilisateur")


i = 0

class MenuTournament:
    tournament_steps = ["Créer un nouveau tournoi", "Enregistrer les joueurs du tournoi",
                        "Afficher les matchs à jouer", "Démarrer la tournée à jouer",
                        "Saisir les scores de la tournée", "Afficher les scores finaux du tournoi"]

    tournament_manager = TournamentManager()

    def __init__(self):
        print("Vous êtes dans le menu pilotage de tournoi\n")

    def choices(self):

        global i
        global NUMBER_ROUNDS

        while i < len(self.tournament_steps):
            choices = [self.tournament_steps[i], "Retour au menu principal"]
            main_choice = pyip.inputMenu(choices, prompt="Saisir le chiffre de l'action désirée :\n", numbered=True)

            if main_choice == "Créer un nouveau tournoi":
                self.tournament = self.tournament_manager.input_tournament_data()
                self.tournament_manager.display_tournament_data(self.tournament)
                i += 1
                self.choices()
            elif main_choice == "Enregistrer les joueurs du tournoi":
                print("test enregistrer les joueurs du tournoi")
                self.tournament_manager.test_tournament_add_players(self.tournament) # à changer avant prod
                i += 1
                self.choices()
            elif main_choice == "Afficher les matchs à jouer":
                self.round_name, self.pairs_players = self.tournament_manager.prepare_round(self.tournament)
                i += 1
                self.choices()
            elif main_choice == "Démarrer la tournée à jouer":
                self.round_ = self.tournament_manager.start_round(self.round_name, self.pairs_players)
                print(f"\nLa tournée {self.round_name} a débuté !\n")
                i += 1
                self.choices()
            elif main_choice == "Saisir les scores de la tournée":
                self.tournament_manager.update_score(self.round_, self.tournament)
                print(f"les scores de la tournée {self.round_.round_name} sont saisis.\nVous pouvez afficher les matchs "
                      f"de la tournée suivante.\n")
                if self.tournament_manager.number_rounds <= NUMBER_ROUNDS:
                    i -= 2
                else:
                    i += 1
                self.choices()
            elif main_choice == "Afficher les scores finaux du tournoi":
                self.tournament_manager.update_tournament_final_scores(self.tournament)
                self.tournament_manager.display_tournament_total_scores(self.tournament)
                i += 1
                self.choices()
            elif main_choice == "Retour au menu principal":
                init_menu = MenuMain()
                init_menu.choices()

        init_menu = MenuMain()
        init_menu.choices()

class MenuPlayer:
    print("Vous êtes dans le menu Player")


class MenuReports:
    print("Vous êtes dans le menu Rapports")
