import pyinputplus as pyip

class MenuPlayers:

    def __init__(self):
        print("Vous êtes dans le menu de gestion des joueurs\n")
        
    def choices(self):
        main_choice = pyip.inputMenu(["Créer un joueur", "Modifier le classement d'un joueur", "Afficher la liste des joueurs"],
                                     prompt="Saisir le chiffre de l'action désirée :\n", numbered=True)
        if main_choice == "Créer un joueur":
            pass
        if main_choice == "Modifier le classement d'un joueur":
            pass
        if main_choice == "Afficher la liste des joueurs":
            pass