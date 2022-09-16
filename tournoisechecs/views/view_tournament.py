from colorama import init, Fore

import pyinputplus as pyip
from datetime import datetime
from operator import attrgetter

init()


class ViewTournament:
    """
    Contains all the methods to input or display tournaments data. These
    methods are called by the methods of the class TournamentManager (module
    controller tournament_manager.
    Class variables:
    - tournament_attrs: a dict with as keys the French items seen by the
    user and as values the relative attributes as initialized in the class
    Tournament (module model tournament).
    - french_tournament_attrs: a list of al French keys extracted from the
    previous dict.
    - tournament_input_function: a dict with the French items as keys and as
    values under string format the methods of pyinputplus the user will
    call to input the values of the attributes. These strings including
    the typo of pyip methods with their parameters will be called by the
     method eval() to be used the relative method.
    """

    tournament_attrs = {"Nom du tournoi": 'tournament_name',
                        "Lieu": 'place',
                        "Date(s)": 'dates_tournament',
                        "Contrôle temps": 'time_control',
                        "Description": 'tournament_description'
                        }

    french_tournament_attrs = list(tournament_attrs.keys())

    tournament_input_function = {"Nom du tournoi": 'pyip.inputStr("Nom du tournoi : ",'
                                                   ' applyFunc=lambda str_: str_.upper())',
                                 "Lieu": 'pyip.inputStr("Lieu du tournoi : ",'
                                         ' applyFunc=lambda str_: str_.upper())',
                                 "Date(s)": 'pyip.inputDatetime("DDate (jjmmaaaa) : ", formats=["%d%m%Y"])',
                                 "Contrôle temps": 'pyip.inputMenu(["Bullet", "Blitz", "Coup rapide"],'
                                                   ' prompt="Saisir le numéro du critère souhaité de saisie :\\n",'
                                                   '  numbered=True)',
                                 }

    def __init__(self, tournaments_instances):
        """Initialize the list of tournaments"""
        self.tournaments_instances = tournaments_instances

    def tournament_selection(self, tournament_selection_data, tournaments_list):
        """
        Allow to select a tournament. The controller tournament_manager
        call the method with an empty dict tournament_selection_data, a
        tournaments_list with all the existing tournaments and a variable
        i equal 0 which value, changed in the process will determine a
        sequence.
        As long as a tournament attribute has no value, the user can choose
        the attribute by calling input_chosen_attr() and when enter a
        searched_value by calling input_search_value. Thanks to
        tournament_search(), the tournaments_list will only contain the
        tournaments corresponding. tournament_selection_data stores the
        entered attributes and values. If no corresponding, tournaments_list
        will be empty and the user can decide to begin again the research
        from scratch or cancel it. If tournaments_list contains only one
        tournament, the user can validate it as searched tournament, if
        not he can begin again the research from scratch or cancel it.
        """

        print(Fore.GREEN+"\nSélection d'un tournoi : \n")

        selected_tournament = []
        tournament = None

        while len(tournament_selection_data) < len(self.tournament_attrs):
            dict_french_english_attr_ = self.input_chosen_attr_(tournament_selection_data)
            french_attr_ = list(dict_french_english_attr_.keys())[0]
            chosen_attr_ = dict_french_english_attr_[french_attr_]

            searched_value = self.input_search_value(french_attr_)

            tournament_selection_data[french_attr_] = searched_value

            tournaments_list = self.tournament_search(tournaments_list, chosen_attr_, searched_value)

            if len(tournaments_list) > 0:
                print("\nListe des tournois correspondants aux critères :\n")
                print(Fore.WHITE)
                for tournament in tournaments_list:
                    print(tournament)

                if len(tournaments_list) == 1:
                    choice = pyip.inputYesNo(prompt=Fore.GREEN+"est-ce le tournoi cherché : Oui(y/Y) / Non(n/N) ?\n")

                    if choice == "yes":

                        for tournament in tournaments_list:
                            selected_tournament.append(tournament)

                        return selected_tournament[0]

                    elif choice == "no":

                        tournaments_list = self.tournaments_instances
                        tournament_selection_data = self.restart_or_cancel()

                        if tournament_selection_data is None:

                            return None

            elif len(tournaments_list) == 0:
                tournament = self.restart_or_cancel()
                if not tournament:
                    break

            else:
                pass

        # return tournament

    def input_chosen_attr_(self, tournament_selection_data):
        """
        check the already used attributes and store their French wordings
        in treated_attrs. Create a comprehension list of the remaining
        attributes. If several remaining submit them to the user for choice,
        else take the only one remaining. Returns a dict with the French
        item as key and the English wording of the attribute as value.
        """

        print(Fore.RED)

        treated_attrs = list(tournament_selection_data.keys())
        remaining_french_tournament_attrs = [attr_ for attr_ in self.french_tournament_attrs + treated_attrs
                                             if attr_ not in self.french_tournament_attrs or attr_ not in treated_attrs
                                             ]
        if len(remaining_french_tournament_attrs) > 1:
            french_attr_ = pyip.inputMenu(remaining_french_tournament_attrs,
                                          prompt="\nSaisir le numéro du critère souhaité de saisie :\n\n",
                                          numbered=True)

        else:
            french_attr_ = remaining_french_tournament_attrs[0]

        chosen_attr_ = self.tournament_attrs[french_attr_]

        return {french_attr_: chosen_attr_}

    def input_search_value(self, french_attr_):
        """Select in the dict tournament_input_function the value
        corresponding to the key french_attr_ and use it as callable
        method thanks to the eval() method. Return the value entered by
        the user on demand of called method."""

        print(Fore.WHITE)

        searched_value = eval(self.tournament_input_function[french_attr_])

        return searched_value

    @staticmethod
    def tournament_search(tournaments_list, chosen_attr_, searched_value):
        """Select the tournaments from tournaments_list having the
         attribute chosen_attr_ with value as value. Returns this list."""

        if chosen_attr_ == 'dates_tournament':

            searched_value = datetime.strftime(searched_value, '%d/%m/%Y')
            tournaments_found = [tournament for tournament in tournaments_list
                                 if searched_value in tournament.dates_tournament
                                 ]

            return tournaments_found

        else:

            getter = attrgetter(chosen_attr_)
            tournaments_found = [tournament for tournament in tournaments_list if getter(tournament) == searched_value]

            return tournaments_found

    @staticmethod
    def restart_or_cancel():
        """If no tournament selected or corresponding ask the user if he
        wants to begin from scratch a research (returns an empty dict)
        or to cancel the research (returns None)"""

        next_choice = pyip.inputYesNo(prompt=Fore.RED+"Pas de tournoi existant.\nVoulez-vous reprendre la recherche"
                                      " oui (y/N) ou non (n/N) ?")

        if next_choice == "no":

            print(Fore.RED+"\nAbandon de la recherche d'un tournoi \n")

            return None

        if next_choice == "yes":

            print(Fore.RED+"\nReprise au début de la recherche d'un tournoi : \n")

            return {}

    @staticmethod
    def input_tournament_data():
        """asks to enter the value needed to create a tournament and
        return a dict with as keys the attributes names and as values the
        inputs"""

        print(Fore.WHITE)

        dates_tournament = []
        tournament_name = pyip.inputStr("\nNom du tournoi : ", applyFunc=lambda str_: str_.upper())
        place = pyip.inputStr("Lieu : ", applyFunc=lambda str_: str_.upper())

        input_date = "yes"
        while input_date == "yes":
            date_tournament = pyip.inputDatetime("Date (jjmmaaaa) : ", formats=['%d%m%Y'])
            dates_tournament.append(datetime.strftime(date_tournament, '%d/%m/%Y'))
            input_date = pyip.inputYesNo(prompt="Voulez-vous ajouter une date au tournoi Oui (y/Y) / Non (n/N) : ")

        time_control = pyip.inputMenu(["Bullet", "Blitz", "Coup rapide"], prompt="Contrôle temps :\n", numbered=True)
        tournament_description = pyip.inputStr("Description du tournoi : ", blank=True)

        return {"tournament_name": tournament_name,
                "place": place,
                "dates_tournament": dates_tournament,
                "time_control": time_control,
                "tournament_description": tournament_description
                }

    @staticmethod
    def display_tournament_data(tournament):
        """Called by the method display_tournament_data() of TournamentManager
        (module controller tournament_manager), display the features of
        a just created tournament"""

        print(Fore.GREEN+f"\nVous avez créé un tournoi avec les informations suivantes :\n")
        print(Fore.WHITE)
        print(f"Nom du tournoi : {tournament.tournament_name}\n"
              f"Lieu du tournoi : {tournament.place}\n"
              f"Date(s) : {tournament.dates_tournament}\n"
              f"Contrôle temps : {tournament.time_control}\n"
              f"Description : {tournament.tournament_description}\n")

    @staticmethod
    def display_tournament(tournament):
        """Called by the method display_tournament() of TournamentManager
        (module controller tournament_manager), display the features of
        a tournament"""

        print(Fore.WHITE, tournament)

    @staticmethod
    def display_tournament_in_progress():  # Vérifier si pas inutile

        print(Fore.RED+"\nCette action n'est pas possible tant que le tournoi n'est pas terminé !\n")

    @staticmethod
    def display_remaining_rounds(remaining_rounds):
        print(Fore.GREEN+f"Il reste {remaining_rounds} tour(s) à jouer pour ce tournoi.\n")

    @staticmethod
    def display_tournament_total_scores(player_data):

        tournament_rank = player_data["tournament_rank"]
        first_name = player_data["first_name"]
        last_name = player_data["last_name"]
        date_birth = player_data["date_birth"]
        rank = player_data["rank"]
        score = player_data["score"]

        print(Fore.WHITE+f"{tournament_rank+1}. {first_name} {last_name} né(e) le {date_birth} classé(e) {rank} -"
                         f" Score : {score}")

    @staticmethod
    def input_tournament_player_new_rank():

        new_rank = pyip.inputInt(prompt="Saisir le nouveau classement du joueur : \n")

        return new_rank
