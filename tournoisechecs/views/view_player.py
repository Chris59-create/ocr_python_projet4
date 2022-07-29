
import random
import pyinputplus as pypi



class ViewPlayer:

    def input_player_data(self):
        first_name = pypi.inputStr("Nom de Famille : ")
        last_name = pypi.inputStr("Prénom : ")
        date_birth = pypi.inputDate("Date de naissance (jjmmaaaa) : ", formats=['%d%m%Y'])
        gender = pypi.inputMenu(["Femme", "Homme", "Autre"], numbered=True)
        rank = pypi.inputInt("Classement : ", default=0, min=0)

        return first_name, last_name, date_birth, gender, rank
