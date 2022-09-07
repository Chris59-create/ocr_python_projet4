import pyinputplus as pyip
from controllers.helpers import console_clear


class ViewRound:

    @staticmethod
    def display_pairs_round(pairs_players):

        print("\nVont jouer lors de ce tour :\n")
        for element in pairs_players:
            print(f"{element[0].first_name} {element[0].last_name} classé {element[0].rank} contre "
                  f"{element[1].first_name} {element[1].last_name} classé {element[1].rank}.")
        print()

    def input_score(self, player1, player2):
        print(f"Joueur 1 : {player1.first_name} {player1.last_name}\nJoueur 2 :"
              f" {player2.first_name} {player2.last_name}")
        print("\nQui a gagné le match ?\n")
        match_winner = pyip.inputMenu(["Joueur 1", "Joueur 2", "Match nul"],
                                      prompt="Saisir le chiffre de l'action désirée : \n\n",
                                      numbered=True
                                      )
        if match_winner == "Joueur 1":
            score_player1 = 1
            score_player2 = 0
        if match_winner == "Joueur 2":
            score_player1 = 0
            score_player2 = 1
        if match_winner == "Match nul":
            score_player1 = 0.5
            score_player2 = 0.5

        print(f"score du match :\n{player1.last_name} : {score_player1}, {player2.last_name} : {score_player2}")

        console_clear(5)

        return score_player1, score_player2
