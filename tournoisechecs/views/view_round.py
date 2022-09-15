from colorama import init, Fore
import pyinputplus as pyip
from controllers.helpers import console_clear

init()


class ViewRound:

    @staticmethod
    def display_pairs_round(pairs_players):

        print(Fore.BLUE+"\nVont jouer lors de ce tour :\n")
        print(Fore.WHITE)

        for element in pairs_players:
            print(f"{element[0].first_name} {element[0].last_name} classé {element[0].rank} contre "
                  f"{element[1].first_name} {element[1].last_name} classé {element[1].rank}.")
        print()

    @staticmethod
    def input_score(self, player1, player2):

        print(Fore.WHITE+f"Joueur 1 : {player1.first_name} {player1.last_name}\nJoueur 2 :"
              f" {player2.first_name} {player2.last_name}")
        print(Fore.BLUE+"\nQui a gagné le match ?\n")
        print(Fore.RED)
        match_winner = pyip.inputMenu(["Joueur 1", "Joueur 2", "Match nul"],
                                      prompt="Saisir le chiffre de l'action désirée : \n\n",
                                      numbered=True
                                      )

        if match_winner == "Joueur 1":
            score_player1 = 1
            score_player2 = 0

        elif match_winner == "Joueur 2":
            score_player1 = 0
            score_player2 = 1

        elif match_winner == "Match nul":
            score_player1 = 0.5
            score_player2 = 0.5

        print(Fore.WHITE+f"score du match :\n{player1.last_name} : {score_player1}, {player2.last_name} : {score_player2}")

        console_clear()

        return score_player1, score_player2

    @staticmethod
    def display_round(round_, round_results):

        print(Fore.BLUE+f"\n{round_.round_name} :\n")

        round_rank = 1
        for player, score in sorted(round_results.items(), key=lambda x: x[1], reverse=True):
            print(Fore.WHITE+f"{round_rank}. {player.last_name} {player.first_name}"
                  f" (né(e le {player.date_birth.strftime('%d/%m/%Y')} - score : {score}")
            round_rank += 1

    @staticmethod
    def display_match(match_result):

        player_1 = list(match_result.keys())[0]
        score_1 = match_result[player_1]
        player_2 = list(match_result.keys())[1]
        score_2 = match_result[player_2]
        date_birth_1 = player_1.date_birth.strftime('%d/%m/%Y')
        date_birth_2 = player_2.date_birth.strftime('%d/%m/%Y')
        print(Fore.WHITE+f"{player_1.last_name} {player_1.first_name} (né(e) le {date_birth_1}) contre"
                         f" {player_2.last_name} {player_2.first_name} (née(e) le {date_birth_2}) :"
                         f" {score_1} - {score_2} ")
