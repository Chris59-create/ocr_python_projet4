import pyinputplus as pypi
from datetime import datetime


class ViewTournament:

    def input_tournament_data(self):
        dates_tournament = []
        tournament_name = pypi.inputStr("Nom du tournoi : ")
        place = pypi.inputStr("Lieu du tournoi : ")

        input_date = True
        while input_date == True:
            date_tournament = pypi.inputDate("Date (jjmmaaaa) : ", formats=['%d%m%Y'])
            dates_tournament.append(datetime.strftime(date_tournament, '%d/%m/%Y'))
            input_date = pypi.inputBool("Voulez-vous ajouter une date au tournoi Oui = t Non = f: ", "True", "False")

        time_control = pypi.inputMenu(["Bullet", "Blitz", "Coup rapide"], numbered=True)
        tournament_description = pypi.inputStr("Description du tournoi : ", blank=True)

        return tournament_name, place, dates_tournament, time_control, tournament_description

    def display_tournament_data(self, tournament):
        
        print()
        print(f"Vous avez créé un tournoi avec les informations suivantes :\n \n"
              f"Nom du tournoi : {tournament.tournament_name}\n"
              f"Lieu du tournoi : {tournament.place}\n"
              f"Date(s) : {tournament.dates_tournament}\n"
              f"Contrôle du temps : {tournament.time_control}\n"
              f"Description : {tournament.tournament_description}")
        print()

