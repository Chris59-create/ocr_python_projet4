import pyinputplus as pyip


class ViewRound:

    def display_pairs_round(self, pairs_players):

        print("\nVont jouer lors de ce tour :\n")
        for element in pairs_players:
            print(f"{element[0].first_name} {element[0].last_name} (ID {element[0].player_id}) classé"
                  f" {element[0].rank} contre {element[1].first_name} {element[1].last_name} (ID"
                  f" {element[1].player_id}) classé {element[1].rank}.")
        print()

    def input_score(self, player1, player2):
        print(f"Joueur 1 : {player1.first_name} {player1.last_name}\nJoueur 2 :"
              f" {player2.first_name} {player2.last_name}")
        print("Qui a gagné le match ?")
        match_winner = pyip.inputMenu(["Joueur 1", "Joueur 2", "Match nul"],
                                      prompt="Saisir le chiffre de l'action désirée : \n",
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

        print(f"score du match :\n{player1.last_name} ID {player1.player_id} : {score_player1}, {player2.last_name} "
              f"ID {player2.player_id} : {score_player2}")

        return score_player1, score_player2
