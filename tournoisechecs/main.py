from controllers.tournament_manager import TournamentManager
from models.player import Player
from views.view_player import ViewPlayer

def main():
    view = ViewPlayer()
    game = TournamentManager(view)
    game.run_test()
    print(game.tournament_players[0].rank)

if __name__ == "__main__":
    main()