import pyinputplus as pypi
import random
from datetime import datetime


class ViewPlayer:

    def manual_input_player(self):
        first_name = pypi.inputStr("Nom de Famille : ")
        last_name = pypi.inputStr("Prénom : ")
        date_birth = pypi.inputDate("Date de naissance (jjmmaaaa) : ", formats=['%d%m%Y'])
        gender = pypi.inputMenu(["Femme", "Homme", "Autre"], numbered=True)
        rank = pypi.inputInt("Classement : ", default=0, min=0)

        return first_name, last_name, date_birth, gender, rank

    def random_input_player(self):
        first_name = "Firstname" + str(random.randint(0, 100))
        last_name = "Lastname" + str(random.randint(0, 100))
        date_string = str(random.randint(10, 30)) + str(random.randint(10, 12)) + str(random.randint(1000, 9999))
        date_birth = datetime.strptime(date_string, '%d%m%Y')
        gender = random.choice(["Femme", "Homme", "Autre"])
        rank = random.randint(0, 1000)

        return first_name, last_name, date_birth, gender, rank

    def input_player_data(self):

        mode = pypi.inputMenu(["Saisie des joueurs", "Génération automatique des joueurs en mode test"],
                              numbered=True)
        if mode == "Saisie des joueurs":
            view = self.manual_input_player()
        if mode == "Génération automatique des joueurs en mode test":
            view = self.random_input_player()

        return view