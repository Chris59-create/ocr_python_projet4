import pyinputplus as pyip
from datetime import datetime
import random




class ViewPlayer:

    def manual_input_player(self):
        first_name = pyip.inputStr("Nom de Famille : ")
        last_name = pyip.inputStr("Prénom : ")
        date_birth = pyip.inputDate("Date de naissance (jjmmaaaa) : ", formats=['%d%m%Y'])
        gender = pyip.inputMenu(["Femme", "Homme", "Autre"], numbered=True)
        rank = pyip.inputInt("Classement : ", default=0, min=0)

        return last_name, first_name, date_birth, gender, rank # à faire un dictionnaire

    def random_input_player(self):
        first_name = "Firstname" + str(random.randint(0, 100))
        last_name = "Lastname" + str(random.randint(0, 100))
        date_string = str(random.randint(10, 30)) + str(random.randint(10, 12)) + str(random.randint(1000, 9999))
        date_birth = datetime.strptime(date_string, '%d%m%Y')
        gender = random.choice(["Femme", "Homme", "Autre"])
        rank = random.randint(0, 1000)

        return last_name, first_name, date_birth, gender, rank # à faire un dictionnaire

    #vérifier si à supprimer
    def input_player_data(self):

        mode = pyip.inputMenu(["Saisie des joueurs", "Génération automatique des joueurs en mode test"],
                              numbered=True)
        if mode == "Saisie des joueurs":
            player_data = self.manual_input_player()
        if mode == "Génération automatique des joueurs en mode test":
            player_data = self.random_input_player()

        return player_data
    
    def input_player_new_rank(self):
        print("\nMettre à jour le classement du joueur : ")
        player_id = pyip.inputInt(prompt="\nSaisir le numéro d'identification  (ID) du joueur : ")
        new_rank = pyip.inputInt(prompt="\nSaisir le nouveau classement du joueur : \n")

        return player_id, new_rank

    def display_all_players_by_rank(self):
        pass


