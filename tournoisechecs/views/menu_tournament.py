import pyinputplus as pyip
from controllers.tournament_manager import TournamentManager
from controllers.menus_manager import MenuManager


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

        choices = [self.tournament_steps[i], "Retour au menu principal"]
        main_choice = pyip.inputMenu(choices, prompt="Saisir le chiffre de l'action désirée :\n", numbered=True)

        if main_choice == "Créer un nouveau tournoi":
            self.tournament = self.tournament_manager.input_tournament_data()
            self.tournament_manager.display_tournament_data(self.tournament)
            i += 1
            self.choices()
        elif main_choice == "Enregistrer les joueurs du tournoi":
            print("test enregistrer les joueurs du tournoi")
            self.tournament_manager.test_add_players(self.tournament) # à changer avant prod
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
                  f"de "
                  f"la "
                  f"tournée suivantes.\n")
            i += 1
            self.choices()
        elif main_choice == "Afficher les scores finaux du tournoi":
            self.tournament_manager.update_tournament_final_scores(self.tournament)
            self.tournament_manager.display_tournament_total_scores(self.tournament)
            i += 1
            self.choices()
        elif main_choice == "Retour au menu principal":
            menus_manager = MenuManager()
            menus_manager.back_to_menu_main()




        i += 1
