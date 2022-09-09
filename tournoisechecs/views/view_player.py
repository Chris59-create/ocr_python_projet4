import pyinputplus as pyip
from operator import attrgetter


class ViewPlayer:

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
                             "Date de naissance": 'pyip.inputDate("Date de naissance (jjmmaaaa) : ",'
                                                  ' formats=["%d%m%Y"])',
                             "Genre": 'pyip.inputMenu(["Femme", "Homme", "Autre"],'
                                      ' prompt="Saisir le numéro du critère souhaité de saisie :\\n",  numbered=True)',
                             "Classement": 'pyip.inputInt("Classement : ", default=0, min=0)'
                             }

    def __init__(self, players_instances):
        self.players_instances = players_instances

    def player_selection(self, player_selection_data, players_list, i):

        print("\nCréation / Sélection d'un joueur pour le tournoi : \n")

        selected_player = []

        while len(player_selection_data) < len(self.player_attrs):
            dict_french_english_attr_ = self.input_chosen_attr_(player_selection_data)
            french_attr_ = list(dict_french_english_attr_.keys())[0]
            chosen_attr_ = dict_french_english_attr_[french_attr_]

            searched_value = self.input_search_value(french_attr_)

            player_selection_data[french_attr_] = searched_value

            players_list = self.player_search(players_list, chosen_attr_, searched_value)

            if len(players_list) > 0:
                print("\nListe des joueurs correspondants aux critères :\n")
                for player in players_list:
                    print(player)

                if len(players_list) == 1:
                    choice = pyip.inputYesNo(prompt="est-ce le joueur cherché : Oui(y/Y) / Non(n/N) ?")
                    if choice == "yes":
                        for player in players_list:
                            selected_player.append(player)
                        player_selection_data = {}
                        player_data = selected_player[0]
                        break
                    elif choice == "no":
                        self.continue_or_restart(player_selection_data)

            elif len(players_list) == 0 and i == 0:
                self.continue_or_restart(player_selection_data)
                i = 1

            else:
                pass

            player_data = dict(zip(self.player_attrs.values(), list(player_selection_data.values())))

        return player_data

    def input_chosen_attr_(self, player_selection_data):
        
        treated_attrs = list(player_selection_data.keys())
        remaining_french_player_attrs = [attr_ for attr_ in self.french_player_attrs + treated_attrs
                                         if attr_ not in self.french_player_attrs or attr_ not in treated_attrs
                                         ]
        if len(remaining_french_player_attrs) > 1:
            french_attr_ = pyip.inputMenu(remaining_french_player_attrs,
                                          prompt="\nSaisir le numéro du critère souhaité de saisie :\n\n",
                                          numbered=True)
            
        else:
            french_attr_ = remaining_french_player_attrs[0]
        chosen_attr_ = self.player_attrs[french_attr_]
        return {french_attr_: chosen_attr_}

    def input_search_value(self, french_attr_):
        
        searched_value = eval(self.player_input_function[french_attr_])
        return searched_value

    @ staticmethod
    def player_search(players_list, chosen_attr_, value):
        
        getter = attrgetter(chosen_attr_)
        players_found = [player for player in players_list if getter(player) == value]

        return players_found

    def continue_or_restart(self, player_selection_data):
        
        next_choice = pyip.inputYesNo(prompt="Pas de joueur existant.\nVoulez-vous saisir les critères restants"
                                             " pour créer un nouveau joueur, oui (y/N) ou non (n/N)")
        if next_choice == "no":
            player_selection_data = {}
            print("\nReprise au début de la saisie des données d'un joueur : \n")
            self.player_selection(player_selection_data, self.players_instances, i=0)
        if next_choice == "yes":
            print("\nContinuation de la saisie des données du joueur : \n")
            self.player_selection(player_selection_data, players_list=[], i=1)

    @staticmethod
    def input_player_new_rank():
        print("\nMettre à jour le classement du joueur : ")
        new_rank = pyip.inputInt(prompt="\nSaisir le nouveau classement du joueur : \n")

        return new_rank

    def display_all_players_by_rank(self):
        pass

    def display_all_players(self):
        for player in self.players_instances:
            print(player)

    @staticmethod
    def display_players(players_sorted, criteria):

        if criteria == "alphabetical":
            print("Liste des joueurs par ordre alphabétique :\n")

        elif criteria == "rank":
            print("Liste des joueurs par classement :\n")

        for player in players_sorted:
            print(player)
