import pyinputplus as pyip
from datetime import datetime
from operator import attrgetter


class ViewTournament:

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
                                 "Date(s)": 'pyip.inputDate("Date du tournoi: ", formats=["%d%m%Y"])',
                                 "Contrôle temps": 'pyip.inputMenu(["Bullet", "Blitz", "Coup rapide"],'
                                                   ' prompt="Saisir le numéro du critère souhaité de saisie :\\n",'
                                                   '  numbered=True)',
                                 }

    def __init__(self, tournaments_instances):
        self.tournaments_instances = tournaments_instances

    def tournament_selection(self, tournament_selection_data, tournaments_list):

        print("\nSélection d'un tournoi : \n")

        selected_tournament = []

        while len(tournament_selection_data) < len(self.tournament_attrs):
            dict_french_english_attr_ = self.input_chosen_attr_(tournament_selection_data)
            french_attr_ = list(dict_french_english_attr_.keys())[0]
            chosen_attr_ = dict_french_english_attr_[french_attr_]

            searched_value = self.input_search_value(french_attr_)

            tournament_selection_data[french_attr_] = searched_value

            tournaments_list = self.tournament_search(tournaments_list, chosen_attr_, searched_value)

            if len(tournaments_list) > 0:
                print("\nListe des tournois correspondants aux critères :\n")
                for tournament in tournaments_list:
                    print(tournament)

                if len(tournaments_list) == 1:
                    choice = pyip.inputYesNo(prompt="est-ce le tournoi cherché : Oui(y/Y) / Non(n/N) ?\n")

                    if choice == "yes":
                        for tournament in tournaments_list:
                            selected_tournament.append(tournament)
                        tournament_selection_data = {}
                        tournament = selected_tournament[0]
                        break

                    elif choice == "no":
                        tournament = self.restart_or_cancel(tournament_selection_data={})
                        if not tournament:
                            break

            elif len(tournaments_list) == 0:
                tournament = self.restart_or_cancel(tournament_selection_data={})
                if not tournament:
                    break

            else:
                pass

        return tournament

    def input_chosen_attr_(self, tournament_selection_data):

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

        searched_value = eval(self.tournament_input_function[french_attr_])
        return searched_value

    @staticmethod
    def tournament_search(tournaments_list, chosen_attr_, value):

        getter = attrgetter(chosen_attr_)
        tournaments_found = [tournament for tournament in tournaments_list if getter(tournament) == value]

        return tournaments_found

    def restart_or_cancel(self, tournament_selection_data):

        next_choice = pyip.inputYesNo(prompt="Pas de tournoi existant.\nVoulez-vous reprendre la recherche"
                                             " oui (y/N) ou non (n/N) ?")

        if next_choice == "no":
            tournament_selection_data = {}
            print("\nAbandon de la recherche d'un tournoi \n")
            tournament = None

        if next_choice == "yes":
            print("\nReprise au début de la recherche d'un tournoi : \n")
            tournament = self.tournament_selection(tournament_selection_data={},
                                                   tournaments_list=self.tournaments_instances)

        return tournament

    @staticmethod
    def input_tournament_data():
        dates_tournament = []
        tournament_name = pyip.inputStr("\nNom du tournoi : ", applyFunc=lambda str_: str_.upper())
        place = pyip.inputStr("Lieu : ", applyFunc=lambda str_: str_.upper())

        input_date = "yes"
        while input_date == "yes":
            date_tournament = pyip.inputDate("Date (jjmmaaaa) : ", formats=['%d%m%Y'])
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

        print()
        print(f"Vous avez créé un tournoi avec les informations suivantes :\n \n"
              f"Nom du tournoi : {tournament.tournament_name}\n"
              f"Lieu du tournoi : {tournament.place}\n"
              f"Date(s) : {tournament.dates_tournament}\n"
              f"Contrôle temps : {tournament.time_control}\n"
              f"Description : {tournament.tournament_description}")
        print()

    @staticmethod
    def display_tournament_in_progress():  # Vérifier si pas inutile
        print("\nCette action n'est pas possible tant que le tournoi n'est pas terminé !\n")

    @staticmethod
    def display_remaining_rounds(remaining_rounds):
        print(f"Il reste {remaining_rounds} tour(s) à jouer pour ce tournoi.\n")

    @staticmethod
    def display_tournament_total_scores(player_data):
        tournament_rank = player_data["tournament_rank"]
        first_name = player_data["first_name"]
        last_name = player_data["last_name"]
        date_birth = player_data["date_birth"]
        rank = player_data["rank"]
        score = player_data["score"]

        print(f"{tournament_rank+1}. {first_name} {last_name} né(e) le {date_birth} classé(e) {rank} - Score : "
              f"{score}")

    @staticmethod
    def input_tournament_player_new_rank():

        new_rank = pyip.inputInt(prompt="Saisir le nouveau classement du joueur : \n")

        return new_rank
