import pyinputplus as pypi


class ViewTournament:

    def input_tournament_data(self):
        tournament_name = pypi.inputStr("Nom du tournoi : ")
        place = pypi.inputStr("Lieu du tournoi : ")
        start_date = pypi.inputDate("Date de début (jjmmaaaa) : ", formats=['%d%m%Y'])
        end_date = pypi.inputDate("Date de fin (jjmmaaaa) : ", formats=['%d%m%Y'])
        time_control = pypi.inputMenu(["Bullet", "Blitz", "Coup rapide"], numbered=True)
        tournament_description = pypi.inputStr("Description du tournoi : ", blank=True)

        return tournament_name, place, start_date, end_date, time_control, tournament_description

    def display_tournament_data(self, tournament):
        pass