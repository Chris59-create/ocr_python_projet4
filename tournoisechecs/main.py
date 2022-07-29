import pyinputplus as pypi
from controllers.tournament_manager import TournamentManager
from models.player import Player
from views.view_player import ViewPlayer
from views.view_player_test import ViewPlayerTest

def main():
    mode = pypi.inputMenu(["Saisie des joueurs", "Génération automatique des joueurs en mode test"],
                               numbered=True)
    if mode == "Saisie des joueurs":
        view = ViewPlayer()
    if mode == "Génération automatique des joueurs en mode test":
        view = ViewPlayerTest()

    game = TournamentManager(view)
    game.run()
    print(game.tournament_players[0].last_name)

if __name__ == "__main__":
    main()