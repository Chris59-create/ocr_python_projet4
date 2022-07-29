from models.tournament import Tournament
from controllers.tournament_manager import TournamentManager
from models.player import Player
from views.view_player import ViewPlayer


def main():
    init_tournament = TournamentManager()
    init_tournament.input_tournament_data()
    init_tournament.add_player()

    print(init_tournament.tournament.tournament_name)
    print(init_tournament.tournament_players[0].last_name)

if __name__ == "__main__":
    main()