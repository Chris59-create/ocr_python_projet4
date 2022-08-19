import pyinputplus as pyip
import sys
from controllers.tournament_manager import TournamentManager, NUMBER_ROUNDS
from controllers.player_manager import PlayerManager
from views.view_tournament import ViewTournament
from views.view_player import ViewPlayer

manage_tournament = None

class MenuMain:

    def __init__(self):
        print("\nMenu principal : \n")

    def manage_tournament(self):

        global manage_tournament

        if isinstance(manage_tournament, MenuTournament):
            manage_tournament.tournament_choices()
        else:
            manage_tournament = MenuTournament()
            manage_tournament.tournament_choices()

    def manage_players(self):
        manage_players = MenuPlayers()
        manage_players.players_choices()

    def edit_reports(self):
        edit_reports = MenuReports()
        edit_reports.reports_choices()

    def main_choices(self):
        main_choice = pyip.inputMenu(["Gérer un tournoi", "Gérer les joueurs", "Editer les rapports",
                                      "Quitter l'application"],
                                     prompt="Saisir le chiffre de l'action désirée : \n\n", numbered=True)
        if main_choice == "Gérer un tournoi":
            self.manage_tournament()
        if main_choice == "Gérer les joueurs":
            self.manage_players()
        if main_choice == "Editer les rapports":
            self.edit_reports()
        if main_choice == "Quitter l'application":
            player_manager = PlayerManager()
            player_manager.save_players_data()

            sys.exit("Application fermée par l'utilisateur")


i = 0

class MenuTournament:
    tournament_steps = ["Créer un nouveau tournoi", "Enregistrer les joueurs du tournoi",
                        "Afficher les matchs à jouer", "Démarrer le tour à jouer",
                        "Saisir les scores du tour", "Afficher les scores finaux du tournoi", "Mettre à jour "
                        "le classement des joueurs"]

    tournament_manager = TournamentManager()

    def __init__(self):
        print("Vous êtes dans le menu pilotage de tournoi\n")

    def tournament_choices(self):

        view_tournament = ViewTournament()

        global i
        global NUMBER_ROUNDS

        while i < len(self.tournament_steps):
            choices = [self.tournament_steps[i], "Retour au menu principal"]
            tournament_choice = pyip.inputMenu(choices, prompt="\nSaisir le chiffre de l'action désirée :\n\n",
                                             numbered=True)

            if tournament_choice == "Créer un nouveau tournoi":
                self.tournament = self.tournament_manager.input_tournament_data()
                self.tournament_manager.display_tournament_data()
                i += 1
                self.tournament_choices()
            elif tournament_choice == "Enregistrer les joueurs du tournoi":
                self.tournament_manager.test_tournament_add_players() # à changer avant prod
                i += 1
                self.tournament_choices()
            elif tournament_choice == "Afficher les matchs à jouer":
                self.round_name, self.pairs_players = self.tournament_manager.prepare_round()
                i += 1
                self.tournament_choices()
            elif tournament_choice == "Démarrer le tour à jouer":
                self.round_ = self.tournament_manager.start_round(self.round_name, self.pairs_players)
                print(f"\nLe tour {self.round_name} a débuté !\n")
                i += 1
                self.tournament_choices()
            elif tournament_choice == "Saisir les scores du tour":
                self.tournament_manager.update_score(self.round_)
                print(f"les scores du tour {self.round_.round_name} sont saisis.\nVous pouvez afficher les matchs "
                      f"du tour suivant.\n")
                if self.tournament_manager.number_rounds <= NUMBER_ROUNDS:
                    i -= 2
                else:
                    i += 1
                self.tournament_choices()
            elif tournament_choice == "Afficher les scores finaux du tournoi":
                self.tournament_manager.update_tournament_final_scores()
                self.tournament_manager.display_tournament_total_scores()
                i += 1
                self.tournament_choices()
            elif tournament_choice == "Mettre à jour le classement des joueurs":
                self.tournament_manager.update_tournament_players_ranks()
                self.tournament_choices()
            elif tournament_choice == "Retour au menu principal":
                init_menu = MenuMain()
                init_menu.main_choices()

        init_menu = MenuMain()
        init_menu.main_choices()

class MenuPlayers:

    player_manager = PlayerManager()

    def __init__(self):
        print("\nVous êtes dans le menu de gestion des joueurs : \n")

    def players_choices(self):
        players_choice = pyip.inputMenu(["Créer un joueur", "Modifier le classement d'un joueur", "Afficher la liste "
                                    "des joueurs", "Retour au menu principal"], prompt="Saisir le chiffre de l'action "
                                    "désirée :\n\n", numbered=True)
        if players_choice == "Créer un joueur":
            self.player_manager.add_single_player()
            self.players_choices()
        if players_choice == "Modifier le classement d'un joueur":
            self.player_manager.update_player_rank()
            self.players_choices()
        if players_choice == "Afficher la liste des joueurs":
            view_player = ViewPlayer()
            view_player.display_all_players(self.player_manager.players_instances)
            self.players_choices()
        if players_choice == "Retour au menu principal":
            init_menu = MenuMain()
            init_menu.main_choices()


class MenuReports:

    def __init__(self):
        print("\nVous êtes dans le menu Rapports\n")

    def reports_choices(self):
        reports_choice = pyip.inputMenu(["Liste des acteurs par ordre alphabétique", "Retour au menu principal"],
                                        prompt="Saisir le chiffre de l'action "
                                    "désirée :\n\n", numbered=True)
        if reports_choice == "Liste des acteurs par ordre alphabétique":

            self.reports_choices()
        if reports_choice == "Modifier le classement d'un joueur":

            self.reports_choices()
        if reports_choice == "Afficher la liste des joueurs":

            self.reports_choices()
        if reports_choice == "Retour au menu principal":
            init_menu = MenuMain()
            init_menu.main_choices()
