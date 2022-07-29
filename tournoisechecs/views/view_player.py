from datetime import datetime
import random
import pyinputplus as pypi


class ViewPlayer:

    def __init__(self):
        input_mode = input

    def input_player_data_manual(self):
        first_name = pypi.inputStr("Nom de Famille : ")
        last_name = pypi.inputStr("Prénom : ")
        date_birth = pypi.inputDate("Date de naissance (jjmmaaaa) : ", formats=['%d%m%Y'])
        gender = pypi.inputMenu(["Femme", "Homme"], lettered=False, numbered=True)
        rank = pypi.inputInt("Classement : ", default=0, min=0)

        return first_name, last_name, date_birth, gender, rank

    def input_player_data_from_dataset(self):
        first_name = "Name" + str(random.randint(0, 100))
        last_name = "Lastname" + str(random.randint(0, 100))
        date_string = str(random.randrange(0, 30)) + str(random.randrange(0, 12)) + str(random.randrange(1000, 9999))
        date_birth = datetime.strptime(date_string, '%d%m%Y')
        gender = random.choice(["F", "H"])
        rank = random.randint(0, 1000)

        return first_name, last_name, date_birth, gender, rank

    def __init__(self):
        pass

