import random
from datetime import datetime


class ViewPlayerTest:

    def generate_test_player(self):
        first_name = "Firstname" + str(random.randint(0, 100))
        last_name = "Lastname" + str(random.randint(0, 100))
        date_string = str(random.randint(10, 30)) + str(random.randint(10, 12)) + str(random.randint(1000, 9999))
        date_birth = datetime.strptime(date_string, '%d%m%Y')
        gender = random.choice(["Femme", "Homme", "Autre"])
        rank = random.randint(0, 1000)

        return first_name, last_name, date_birth, gender, rank

    def input_player_data(self):
        return self.generate_test_player()
