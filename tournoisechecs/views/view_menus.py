import sys
import pyinputplus as pyip
from controllers.helpers import console_clear
from controllers.db_manager import TablePlayers
from controllers.db_manager import TableTournament
from controllers.player_manager import PlayerManager
from controllers.tournament_manager import TournamentManager, NUMBER_ROUNDS


class MenuMain:

    @staticmethod
    def manage_tournament(manage_tournament=None):

        if isinstance(manage_tournament, MenuTournament):
            manage_tournament.tournament_choices()
        else:
            manage_tournament = MenuTournament()
            manage_tournament.tournament_choices()

    @staticmethod
    def manage_players():

        manage_players = MenuPlayers()
        manage_players.players_choices()

    @staticmethod
    def edit_reports():

        edit_reports = MenuReports()
        edit_reports.reports_choices()

    def main_choices(self):

        print("\nMenu principal : \n")

        main_choice = pyip.inputMenu(["Gérer un tournoi", "Gérer les joueurs", "Editer les rapports",
                                      "Quitter l'application"],
                                     prompt="Saisir le chiffre de l'action désirée : \n\n", numbered=True)

        if main_choice == "Gérer un tournoi":

            console_clear()
            self.manage_tournament()
        if main_choice == "Gérer les joueurs":

            console_clear()
            self.manage_players()
        if main_choice == "Editer les rapports":

            console_clear()
            self.edit_reports()
        if main_choice == "Quitter l'application":
            console_clear()
            table_players = TablePlayers()
            table_players.save_players_data()
            sys.exit("Application fermée par l'utilisateur")


class MenuTournament:

    tournament_steps = ["Créer un nouveau tournoi", "Enregistrer les joueurs du tournoi",
                        "Afficher les matchs à jouer", "Démarrer le tour à jouer",
                        "Saisir les scores du tour", "Afficher les scores finaux du tournoi", "Mettre à jour "
                        "le classement des joueurs"]

    tournament_manager = TournamentManager()
    
    i = 0

    def __init__(self):
        self.table_tournament = TableTournament()
        self.table_tournament.install_tournament_data()

        self.tournament = None
        self.round_name = None
        self.pairs_players = None
        self.round_ = None
        self.tournament_final_scores_sorted = None

    def tournament_choices(self):

        print("Vous êtes dans le menu pilotage de tournoi\n")

        while self.i < len(self.tournament_steps):

            choices = [self.tournament_steps[self.i],
                       "Modifier le classement d'un joueur",
                       "Sauvegarder les données du tournoi",
                       "Retour au menu principal"]
            tournament_choice = pyip.inputMenu(choices, prompt="\nSaisir le chiffre de l'action désirée :\n\n",
                                               numbered=True)

            if tournament_choice == "Créer un nouveau tournoi":

                self.tournament = self.tournament_manager.input_tournament_data()
                console_clear()
                self.tournament_manager.display_tournament_data(self.tournament)
                self.i = 1
                self.tournament_choices()

            elif tournament_choice == "Enregistrer les joueurs du tournoi":

                console_clear()
                self.tournament_manager.tournament_add_players(self.tournament)
                self.i += 1
                self.tournament_choices()

            elif tournament_choice == "Afficher les matchs à jouer":

                console_clear()
                self.round_name, self.pairs_players = self.tournament_manager.prepare_round(self.tournament)
                self.i += 1
                self.tournament_choices()

            elif tournament_choice == "Démarrer le tour à jouer":

                console_clear()
                self.round_ = self.tournament_manager.start_round(self.round_name, self.pairs_players)
                print(f"\nLe tour {self.round_name} a débuté !"
                      f" Date et heure de début : {self.round_.start_date_time}\n")
                self.i += 1
                console_clear()
                self.tournament_choices()

            elif tournament_choice == "Saisir les scores du tour":
                console_clear()
                self.tournament_manager.update_score(self.tournament, self.round_)

                if self.tournament_manager.number_rounds <= NUMBER_ROUNDS:
                    print(f"les scores du tour {self.round_name} sont saisis.\nVous pouvez afficher les matchs "
                          f"du tour suivant.\n")
                    self.i -= 2
                else:
                    self.i += 1
                    self.tournament_manager.number_rounds = 1

                self.tournament_manager.display_rounds(self.tournament, self.round_name)

                self.tournament_choices()

            elif tournament_choice == "Afficher les scores finaux du tournoi":

                console_clear()
                remaining_rounds = self.tournament_manager.update_tournament_final_scores(self.tournament)
                self.tournament_final_scores_sorted = self.tournament_manager.display_tournament_total_scores(
                    self.tournament, remaining_rounds)
                self.i += 1
                self.tournament_choices()

            elif tournament_choice == "Mettre à jour le classement des joueurs":

                console_clear()
                self.tournament_manager.update_tournament_players_ranks(self.tournament_final_scores_sorted)
                self.i = 0
                manage_tournament = None
                self.tournament_choices()
                return manage_tournament

            elif tournament_choice == "Modifier le classement d'un joueur":

                console_clear()
                player_manager = PlayerManager()
                player_manager.update_player_rank()
                self.i += 1
                self.tournament_choices()

            elif tournament_choice == "Sauvegarder les données du tournoi":

                console_clear()
                table_tournament = TableTournament()
                table_tournament.save_tournaments_data()
                self.i += 1
                self.tournament_choices()

            elif tournament_choice == "Retour au menu principal":

                console_clear()
                table_tournament = TableTournament()
                table_tournament.save_tournaments_data()
                init_menu = MenuMain()
                init_menu.main_choices()


class MenuPlayers:

    def __init__(self):
        self.player_manager = PlayerManager()

    def players_choices(self):

        print("\nVous êtes dans le menu de gestion des joueurs : \n")

        players_choice = pyip.inputMenu(["Créer un joueur", "Modifier le classement d'un joueur",
                                         "Afficher la liste des joueurs", "Sauvegarder les données joueurs",
                                         "Retour au menu principal"
                                         ],
                                        prompt="Saisir le chiffre de l'action désirée :\n\n", numbered=True)

        if players_choice == "Créer un joueur":

            console_clear()
            self.player_manager.add_player()
            self.players_choices()

        if players_choice == "Modifier le classement d'un joueur":

            console_clear()
            self.player_manager.update_player_rank()
            self.players_choices()

        if players_choice == "Afficher la liste des joueurs":

            console_clear()
            self.player_manager.display_players(self.player_manager.players_instances, 'alphabetical')
            self.players_choices()

        if players_choice == "Sauvegarder les données joueurs":

            console_clear()
            table_players_manager = TablePlayers()
            table_players_manager.save_players_data()
            self.players_choices()

        if players_choice == "Retour au menu principal":

            console_clear()
            init_menu = MenuMain()
            init_menu.main_choices()


class MenuReports:

    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.table_tournament = TableTournament()
        self.table_tournament.install_tournament_data()

    def reports_choices(self):

        print("\nVous êtes dans le menu Rapports\n")

        reports_choice = pyip.inputMenu(["Liste alphabétique des acteurs",
                                         "Liste des acteurs par classement",
                                         "Liste alphabétique des joueurs d'un tournoi",
                                         "Liste de tous les tournois",
                                         "Liste  par classement des joueurs d'un tournoi",
                                         "Liste de tous les tours d'un tournoi",
                                         "Liste de tous les matchs d'un tournoi",
                                         "Retour au menu principal"
                                         ],
                                        prompt="Saisir le chiffre de l'action désirée :\n\n", numbered=True
                                        )

        if reports_choice == "Liste alphabétique des acteurs":

            console_clear()
            self.player_manager.display_players(self.player_manager.players_instances, "alphabetical")
            self.reports_choices()

        if reports_choice == "Liste des acteurs par classement":

            console_clear()
            self.player_manager.display_players(self.player_manager.players_instances, "rank")
            self.reports_choices()

        if reports_choice == "Liste alphabétique des joueurs d'un tournoi":

            console_clear()
            tournament = self.tournament_manager.select_tournament()

            if tournament:
                self.player_manager.display_players(tournament.tournament_players, "alphabetical")

            self.reports_choices()

        if reports_choice == "Liste de tous les tournois":

            console_clear()

            for tournament in self.tournament_manager.tournaments_instances:
                self.tournament_manager.display_tournament(tournament)

            self.reports_choices()

        if reports_choice == "Liste de tous les tours d'un tournoi":

            console_clear()
            tournament = self.tournament_manager.select_tournament()

            if tournament:
                self.tournament_manager.display_rounds(tournament)

            self.reports_choices()

        if reports_choice == "Liste  par classement des joueurs d'un tournoi":

            console_clear()
            tournament = self.tournament_manager.select_tournament()

            if tournament:
                self.player_manager.display_players(tournament.tournament_players, "rank")

            self.reports_choices()

        if reports_choice == "Liste de tous les matchs d'un tournoi":

            console_clear()
            tournament = self.tournament_manager.select_tournament()

            if tournament:
                self.tournament_manager.display_matches(tournament)

            self.reports_choices()

        if reports_choice == "Retour au menu principal":
            init_menu = MenuMain()
            init_menu.main_choices()
