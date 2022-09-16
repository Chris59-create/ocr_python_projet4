import sys

from colorama import init, Fore, Back
import pyinputplus as pyip

from controllers.db_manager import TablePlayers
from controllers.helpers import console_clear
from controllers.player_manager import PlayerManager
from controllers.tournament_manager import TournamentManager, NUMBER_ROUNDS

init()

"""
The contents to navigate in the app and snap actions.
four classes : MenuMain, MenuTournament, MenuPlayers, MenuReports
"""


class MenuMain:
    """The hub to move through the three users issues and relative classes
     and methods """

    @staticmethod
    def check_data_status(table_tournament):
        """Check if the tournament data already uploaded from the table
        tournaments in db.json. To avoid duplicated data. If not: uploads.
        Otherwise : pass. Method called by methods of others classes of
        this module"""

        if table_tournament.data_loaded == 0:
            table_tournament.install_tournament_data()
            table_tournament.data_loaded = 1

        elif table_tournament.data_loaded == 1:
            pass

    @staticmethod
    def manage_tournament(table_tournament, manage_tournament=None):
        """calls the tournament menu after checking if about a tournament
         in progress or a new one."""

        if isinstance(manage_tournament, MenuTournament):
            manage_tournament.tournament_choices(table_tournament)

        else:
            manage_tournament = MenuTournament()
            manage_tournament.tournament_choices(table_tournament)

    @staticmethod
    def manage_players(table_tournament):
        """calls the players menu"""

        manage_players = MenuPlayers()
        manage_players.players_choices(table_tournament)

    @staticmethod
    def edit_reports(table_tournament):
        """calls the reports menu"""

        edit_reports = MenuReports()
        edit_reports.reports_choices(table_tournament)

    def main_choices(self, table_tournament):
        """
        Gives access to the methods calling tournament menu, players menu
        and reports menu. Allow to leave the app with backup of players data.
        Instantiated in the main file table_tournament is  passed as argument
        in all method to be able to check the status of upload of tournament
        data at all steps of the app.
        """

        print(Fore.MAGENTA+"\nMenu principal : \n")
        print(Fore.RED)

        main_choice = pyip.inputMenu(["Gérer un tournoi", "Gérer les joueurs", "Editer les rapports",
                                      "Quitter l'application"],
                                     prompt="Saisir le chiffre de l'action désirée : \n\n", numbered=True)

        if main_choice == "Gérer un tournoi":

            console_clear()
            self.manage_tournament(table_tournament)

        elif main_choice == "Gérer les joueurs":

            console_clear()
            self.manage_players(table_tournament)

        elif main_choice == "Editer les rapports":

            console_clear()
            self.edit_reports(table_tournament)

        elif main_choice == "Quitter l'application":
            console_clear()
            table_players = TablePlayers()
            table_players.save_players_data()
            print(Fore.RESET)
            print(Back.RESET)
            sys.exit("Application fermée par l'utilisateur")


class MenuTournament:
    """
    Through its method tournament_choices manage all the steps of
    tournament in progress.
    Class variables:
    Tournament_steps :  list of the steps of a tournament in progress.
                        Iterated in tournament°choices()
    tournament_manager: instantiated as an TournamentManager object. Allow
                        calling of the methods of this class according
                        user input with tournament_choices.
    i:                  initialize the increment necessary to follow the
                        next tournament step to manage.
    """

    tournament_steps = ["Créer un nouveau tournoi", "Enregistrer les joueurs du tournoi",
                        "Afficher les matchs à jouer", "Démarrer le tour à jouer",
                        "Saisir les scores du tour", "Afficher les scores finaux du tournoi", "Mettre à jour "
                        "le classement des joueurs"]

    tournament_manager = TournamentManager()

    i = 0

    def __init__(self):

        self.init_menu = MenuMain()
        self.tournament = None
        self.round_name = None
        self.pairs_players = None
        self.round_ = None
        self.tournament_final_scores_sorted = None

    def tournament_choices(self, table_tournament):
        """
        Iterate the possible action gradually according the already realized
        steps of the tournament management thanks to the incremental variable i.
        The choice of an option calls a self method which will call relative
        methods in the class TournamentManager in controller module
        tournament_manager;
        """

        print(Fore.MAGENTA+"Vous êtes dans le menu pilotage de tournoi\n")
        print(Fore.RED)

        while self.i < len(self.tournament_steps):

            choices = [self.tournament_steps[self.i],
                       "Modifier le classement d'un joueur",
                       "Sauvegarder les données du tournoi",
                       "Retour au menu principal"]
            tournament_choice = pyip.inputMenu(choices, prompt="\nSaisir le chiffre de l'action désirée :\n\n",
                                               numbered=True)

            if tournament_choice == "Créer un nouveau tournoi":
                self.create_tournament(table_tournament)

            elif tournament_choice == "Enregistrer les joueurs du tournoi":
                self.register_players(table_tournament)

            elif tournament_choice == "Afficher les matchs à jouer":
                self.display_matches(table_tournament)

            elif tournament_choice == "Démarrer le tour à jouer":
                self.start_round(table_tournament)

            elif tournament_choice == "Saisir les scores du tour":
                self.enter_round_results(table_tournament)

            elif tournament_choice == "Afficher les scores finaux du tournoi":
                self.display_end_results(table_tournament)

            elif tournament_choice == "Mettre à jour le classement des joueurs":
                self.update_ranks(table_tournament)

            elif tournament_choice == "Modifier le classement d'un joueur":
                self.change_rank(table_tournament)

            elif tournament_choice == "Sauvegarder les données du tournoi":
                self.backup_tournament_data(table_tournament)

            elif tournament_choice == "Retour au menu principal":
                self.return_main_menu(table_tournament)

    def create_tournament(self, table_tournament):

        self.tournament = self.tournament_manager.input_tournament_data()
        console_clear()
        self.tournament_manager.display_tournament_data(self.tournament)
        self.i = 1
        self.tournament_choices(table_tournament)

    def register_players(self, table_tournament):

        console_clear()
        self.tournament_manager.tournament_add_players(self.tournament)
        self.i += 1
        self.tournament_choices(table_tournament)

    def display_matches(self, table_tournament):

        console_clear()
        self.round_name, self.pairs_players = self.tournament_manager.prepare_round(self.tournament)
        self.i += 1
        self.tournament_choices(table_tournament)

    def start_round(self, table_tournament):

        console_clear()
        self.round_ = self.tournament_manager.start_round(self.round_name, self.pairs_players)
        print(Fore.BLUE + f"\nLe tour {self.round_name} a débuté !"
                          f" Date et heure de début : {self.round_.start_date_time}\n")
        self.i += 1
        console_clear()
        self.tournament_choices(table_tournament)

    def enter_round_results(self, table_tournament):

        console_clear()
        self.tournament_manager.update_score(self.tournament, self.round_)

        if self.tournament_manager.number_rounds <= NUMBER_ROUNDS:

            print(Fore.BLUE + f"les scores du tour {self.round_name} sont saisis."
                              f"\nVous pouvez afficher les matchs du tour suivant.\n")
            self.i -= 2

        else:

            self.i += 1
            self.tournament_manager.number_rounds = 1

        self.tournament_manager.display_rounds(self.tournament, self.round_name)

        self.tournament_choices(table_tournament)

    def display_end_results(self, table_tournament):

        console_clear()
        remaining_rounds = self.tournament_manager.update_tournament_final_scores(self.tournament)
        self.tournament_final_scores_sorted = self.tournament_manager.display_tournament_total_scores(
            self.tournament, remaining_rounds)
        self.i += 1
        self.tournament_choices(table_tournament)

    def update_ranks(self, table_tournament):

        console_clear()
        self.tournament_manager.update_tournament_players_ranks(self.tournament_final_scores_sorted)
        self.i = 0
        self.tournament_choices(table_tournament)

    def change_rank(self, table_tournament):

        console_clear()
        player_manager = PlayerManager()
        player_manager.update_player_rank()
        self.i += 0
        self.tournament_choices(table_tournament)

    def backup_tournament_data(self, table_tournament):

        console_clear()
        self.init_menu.check_data_status(table_tournament)
        table_tournament.save_tournaments_data()
        self.i += 0
        self.tournament_choices(table_tournament)

    def return_main_menu(self, table_tournament):

        console_clear()
        self.init_menu.check_data_status(table_tournament)
        table_tournament.save_tournaments_data()
        self.init_menu.main_choices(table_tournament)


class MenuPlayers:
    """
    Through its players_choices method manage all the possibles actions
    about players.
    Instantiate as attribute player_manager as object of the class
    PlayerManager (controller player_manager) to allow the call of the
    necessary according the action selected by the user
    """

    def __init__(self):
        self.player_manager = PlayerManager()

    def players_choices(self, table_tournament):

        print(Fore.MAGENTA+"\nVous êtes dans le menu de gestion des joueurs : \n")
        print(Fore.RED)

        players_choice = pyip.inputMenu(["Créer un joueur", "Modifier le classement d'un joueur",
                                         "Afficher la liste des joueurs", "Sauvegarder les données joueurs",
                                         "Retour au menu principal"
                                         ],
                                        prompt="Saisir le chiffre de l'action désirée :\n\n", numbered=True)

        if players_choice == "Créer un joueur":

            console_clear()
            self.player_manager.add_player()
            self.players_choices(table_tournament)

        elif players_choice == "Modifier le classement d'un joueur":

            console_clear()
            self.player_manager.update_player_rank()
            self.players_choices(table_tournament)

        elif players_choice == "Afficher la liste des joueurs":

            console_clear()
            self.player_manager.display_players(self.player_manager.players_instances, 'alphabetical')
            self.players_choices(table_tournament)

        elif players_choice == "Sauvegarder les données joueurs":

            console_clear()
            table_players_manager = TablePlayers()
            table_players_manager.save_players_data()
            self.players_choices(table_tournament)

        elif players_choice == "Retour au menu principal":

            console_clear()
            init_menu = MenuMain()
            init_menu.main_choices(table_tournament)


class MenuReports:
    """
    Through its report_choices method allow to display several lists.Each
    user choice call a self method which will call the necessary methods
    of the classes TournamentManager (controller tournament_manager),
    PlayerManager (controller player_manager)
    """

    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.init_menu = MenuMain()

    def reports_choices(self, table_tournament):

        print(Fore.MAGENTA+"\nVous êtes dans le menu Rapports\n")
        print(Fore.RED)

        reports_choice = pyip.inputMenu(["Liste alphabétique des acteurs",
                                         "Liste des acteurs par classement",
                                         "Liste de tous les tournois",
                                         "Liste alphabétique des joueurs d'un tournoi",
                                         "Liste par classement des joueurs d'un tournoi",
                                         "Liste de tous les tours d'un tournoi",
                                         "Liste de tous les matchs d'un tournoi",
                                         "Retour au menu principal"
                                         ],
                                        prompt="Saisir le chiffre de l'action désirée :\n\n", numbered=True
                                        )

        if reports_choice == "Liste alphabétique des acteurs":
            self.list_all_players_alphabetical(table_tournament)

        elif reports_choice == "Liste des acteurs par classement":
            self.list_all_players_by_rank(table_tournament)

        elif reports_choice == "Liste de tous les tournois":
            self.list_all_tournaments(table_tournament)

        elif reports_choice == "Liste alphabétique des joueurs d'un tournoi":
            self.list_tournament_players_alphabetical(table_tournament)

        elif reports_choice == "Liste par classement des joueurs d'un tournoi":
            self.list_tournament_players_by_rank(table_tournament)

        elif reports_choice == "Liste de tous les tours d'un tournoi":
            self.list_tournament_rounds(table_tournament)

        elif reports_choice == "Liste de tous les matchs d'un tournoi":
            self.list_tournament_matches(table_tournament)

        elif reports_choice == "Retour au menu principal":

            console_clear()
            init_menu = MenuMain()
            init_menu.main_choices(table_tournament)

    def list_all_players_alphabetical(self, table_tournament):

        console_clear()
        self.player_manager.display_players(self.player_manager.players_instances, "alphabetical")
        self.reports_choices(table_tournament)

    def list_all_players_by_rank(self, table_tournament):

        console_clear()
        self.player_manager.display_players(self.player_manager.players_instances, "rank")
        self.reports_choices(table_tournament)

    def list_all_tournaments(self, table_tournament):

        console_clear()

        self.init_menu.check_data_status(table_tournament)

        for tournament in self.tournament_manager.tournaments_instances:
            self.tournament_manager.display_tournament(tournament)

        self.reports_choices(table_tournament)

    def list_tournament_players_alphabetical(self, table_tournament):

        console_clear()
        self.init_menu.check_data_status(table_tournament)

        tournament = self.tournament_manager.select_tournament()

        if tournament:
            self.player_manager.display_players(tournament.tournament_players, "alphabetical")

        self.reports_choices(table_tournament)

    def list_tournament_players_by_rank(self, table_tournament):

        console_clear()
        self.init_menu.check_data_status(table_tournament)
        tournament = self.tournament_manager.select_tournament()

        if tournament:
            self.player_manager.display_players(tournament.tournament_players, "rank")

        self.reports_choices(table_tournament)

    def list_tournament_rounds(self, table_tournament):

        console_clear()
        self.init_menu.check_data_status(table_tournament)
        tournament = self.tournament_manager.select_tournament()

        if tournament:
            self.tournament_manager.display_rounds(tournament)

        self.reports_choices(table_tournament)

    def list_tournament_matches(self, table_tournament):

        console_clear()
        self.init_menu.check_data_status(table_tournament)
        tournament = self.tournament_manager.select_tournament()

        if tournament:
            self.tournament_manager.display_matches(tournament)

        self.reports_choices(table_tournament)
