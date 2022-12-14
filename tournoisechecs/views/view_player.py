from colorama import init, Fore

import pyinputplus as pyip
from operator import attrgetter

init()


class ViewPlayer:
    """
    Contains all the methods to input or display players data. These
    methods are called by the methods of the class PlayerManager (module
    controller player_manager.
    Class variables:
    - player_attrs: a dict with as keys the French items seen by the user
    and as values the relative attributes as initialized in the class Player
    (module model player).
    - french_player_attrs: a list of al French keys extracted from the
    previous dict.
    - player_input_function: a dict with the French items as keys and as
    values under string format the methods of pyinputplus the user will
    call to input the values of the attributes. These strings including
    the typo of pyip methods with their parameters will be called by the
     method eval() to be used the relative method.
    """

    player_attrs = {"Nom de famille": 'last_name',
                    "Prénom": 'first_name',
                    "Date de naissance": 'date_birth',
                    "Genre": 'gender',
                    "Classement": 'rank'
                    }

    french_player_attrs = list(player_attrs.keys())

    player_input_function = {"Nom de famille": 'pyip.inputStr("Nom de Famille : ",'
                                               ' applyFunc=lambda str_: str_.upper())',
                             "Prénom": 'pyip.inputStr("Prénom : ", applyFunc=lambda str_: str_.upper())',
                             "Date de naissance": 'pyip.inputDatetime("Date de naissance (jjmmaaaa) : ",'
                                                  ' formats=["%d%m%Y"])',
                             "Genre": 'pyip.inputMenu(["Femme", "Homme", "Autre"],'
                                      ' prompt="Saisir le numéro du critère souhaité de saisie :\\n",  numbered=True)',
                             "Classement": 'pyip.inputInt("Classement : ", default=0, min=0)'
                             }

    def __init__(self, players_instances):
        """Initialize the list of players with all players"""
        self.players_instances = players_instances

    def player_selection(self, player_selection_data, players_list, i):
        """
        Allow to select a player if exit or if not to create one.
        The controller player_manager call the method with an empty dict
        player_selection_data, a players_list with all the existing
        players and a variable i equal 0 which value, changed in the
        process will determine a sequence.
        As long as a player attribute has no value, the user can choose
        the attribute by calling input_chosen_attr() and when enter a
        searched_value by calling input_search_value. Thanks to
        player_search(), the players_list will only contain the players
        corresponding. player_selection_data stores the entered attributes
        and values. If no corresponding, players_list will be empty and
        the user can decide to enter the remaining attributes to create a
        new player, begin again the research from scratch or cancel it
        If players_list contains only one player, the user can validate
        it as research player, if not he can enter the remaining
        attributes to create a new player, begin again the research from
        scratch or cancel it.
        """

        print(Fore.GREEN+"\nCréation / Sélection d'un joueur pour le tournoi : \n")

        selected_player = []

        while len(player_selection_data) < len(self.player_attrs):

            dict_french_english_attr_ = self.input_chosen_attr_(player_selection_data)
            french_attr_ = list(dict_french_english_attr_.keys())[0]
            chosen_attr_ = dict_french_english_attr_[french_attr_]

            searched_value = self.input_search_value(french_attr_)

            player_selection_data[french_attr_] = searched_value

            players_list = self.player_search(players_list, chosen_attr_, searched_value)

            if len(players_list) > 0:

                print(Fore.GREEN+"\nListe des joueurs correspondants aux critères :\n")

                for player in players_list:
                    print(Fore.WHITE, player)

                if len(players_list) == 1:

                    choice = pyip.inputYesNo(prompt=Fore.RED+"est-ce le joueur cherché : Oui(y/Y) / Non(n/N) ?")

                    if choice == "yes":

                        for player in players_list:
                            selected_player.append(player)

                        return selected_player[0]

                    elif choice == "no":

                        players_list = self.players_instances
                        player_selection_data = self.continue_or_restart(player_selection_data)

                        if player_selection_data is None:

                            return None

            elif len(players_list) == 0 and i == 0:

                player_selection_data = self.continue_or_restart(player_selection_data)
                i = 1

                if player_selection_data is None:

                    return None

        player_data = dict(zip(self.player_attrs.values(), list(player_selection_data.values())))

        return player_data

    def input_chosen_attr_(self, player_selection_data):
        """
        check the already used attributes and store their French wordings
        in treated_attrs. Create a comprehension list of the remaining
        attributes. If several remaining submit them to the user for choice,
        else take the only one remaining. Returns a dict with the French
        item as key and the English wording of the attribute as value.
        """

        print(Fore.RED)

        treated_attrs = list(player_selection_data.keys())
        remaining_french_player_attrs = [attr_ for attr_ in self.french_player_attrs + treated_attrs
                                         if attr_ not in self.french_player_attrs or attr_ not in treated_attrs
                                         ]
        if len(remaining_french_player_attrs) > 1:

            print(Fore.RED)
            french_attr_ = pyip.inputMenu(remaining_french_player_attrs,
                                          prompt="\nSaisir le numéro du critère souhaité de saisie :\n\n",
                                          numbered=True)

        else:

            french_attr_ = remaining_french_player_attrs[0]

        chosen_attr_ = self.player_attrs[french_attr_]

        return {french_attr_: chosen_attr_}

    def input_search_value(self, french_attr_):
        """Select in the dict player_input_function the value corresponding
        to the key french_attr_ and use it as callable method thanks to
        the eval() method. Return the value entered by the user on demand
        of called method."""

        print(Fore.WHITE)
        searched_value = eval(self.player_input_function[french_attr_])

        return searched_value

    @ staticmethod
    def player_search(players_list, chosen_attr_, value):
        """Select the players from players_list having the attribute
        chosen_attr_ with value as value. Returns this list."""

        getter = attrgetter(chosen_attr_)
        players_found = [player for player in players_list if getter(player) == value]

        return players_found

    @staticmethod
    def continue_or_restart(player_selection_data):
        """If no player selected or corresponding ask the user if he wants
        to enter the remaining criteria (returns when the dict with the
         already entered criteria and values), to begin from scratch a research
         (returns an empty dict) or to cancel the research (returns None)"""

        next_choices = ["Saisie des critères restants pour créer un nouveau joueur.",
                        "Reprise au début de la saisie des données d'un joueur.",
                        "Abandon de la création / sélection d'un joueur."
                        ]
        message = "\nPas de joueur existant!\nSaisir le numéro du critère souhaité de saisie :\n\n"

        print(Fore.RED)
        next_choice = pyip.inputMenu(next_choices, prompt=message, numbered=True)

        if next_choice == "Saisie des critères restants pour créer un nouveau joueur.":

            print(Fore.GREEN+"\nSaisie des critères restants pour créer un nouveau joueur : \n")

            return player_selection_data

        elif next_choice == "Reprise au début de la saisie des données d'un joueur.":

            print(Fore.GREEN+"\nReprise au début de la saisie des données d'un joueur : \n")

            return {}

        elif next_choice == "Abandon de la création / sélection d'un joueur.":

            return None

    @staticmethod
    def input_player_new_rank():
        """Called by a method of the controller player_manager, allows
        to enter a new rank value"""

        print(Fore.GREEN+"\nMettre à jour le classement du joueur : ")

        new_rank = pyip.inputInt(prompt=Fore.RED+"\nSaisir le nouveau classement du joueur : \n")

        return new_rank

    @staticmethod
    def display_players(players_sorted, criteria):
        """called by the relative method of the controller player_manager,
         displays the title of the list and the demanded list."""

        if criteria == "alphabetical":
            print(Fore.GREEN+"Liste des joueurs par ordre alphabétique :\n")

        elif criteria == "rank":
            print(Fore.GREEN+"Liste des joueurs par classement :\n")

        for player in players_sorted:
            print(Fore.WHITE, player)
