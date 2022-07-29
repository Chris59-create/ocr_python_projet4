
NUMBER_ROUNDS = 4
ROUNDS_NAMES = [f"round{i}" for i in range(1, NUMBER_ROUNDS+1)]

class Tournament:
    def __init__(self, tournament_name, place, start_date, end_date, time_control, tournament_description=""):
        self.tournament_name = tournament_name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.tournament_description = tournament_description
        self.rounds = []
        self.tournament_players = []

    def add_player(self, player):
        self.tournament_players.append(player)

    def add_round(self, round):
        self.rounds.append(round)