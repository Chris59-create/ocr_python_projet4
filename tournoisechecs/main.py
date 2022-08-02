from controllers.tournament_manager import TournamentManager


def main():
    init_tournament = TournamentManager()
    init_tournament.run_tournament_test()


if __name__ == "__main__":
    main()