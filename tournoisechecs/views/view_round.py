import pyinputplus as pypi


class ViewRound:

    def display_pairs_round(self, pairs_players):

        print("\nVont jouer lors de ce tour :\n")
        for element in pairs_players:
            print(f"{element[0].first_name} {element[0].last_name} classé {element[0].rank} contre"
                  f" {element[1].first_name}"
                  f" {element[1].last_name}"
                  f" classé {element[1].rank}.")
        print()

    def input_score(self, joueur1, joueur2):
        print(joueur1.first_name, joueur1.last_name, " contre ", joueur2.first_name, joueur2.last_name)
        print("Qui a gagné le match ?")
        match_winner = pypi.inputMenu([f"{joueur1.last_name}", f"{joueur2.last_name}", "Match nul"], numbered=True)
        if match_winner == joueur1.last_name:
            score_joueur1 = 1
            score_joueur2 = 0
        if match_winner == joueur2.last_name:
            score_joueur1 = 0
            score_joueur2 = 1
        if match_winner == "Match nul":
            score_joueur1 = 0.5
            score_joueur2 = 0.5

        print(f"{joueur1.last_name} : {score_joueur1}, {joueur2.last_name} : {score_joueur2}")

        return score_joueur1, score_joueur2
