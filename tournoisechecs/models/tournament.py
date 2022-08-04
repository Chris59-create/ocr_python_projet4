
NUMBER_ROUNDS = 4
ROUNDS_NAMES = [f"round{i}" for i in range(1, NUMBER_ROUNDS+1)]

class Tournament:
    def __init__(self, tournament_name, place, dates_tournament, time_control, tournament_description=""):
        self.tournament_name = tournament_name
        self.place = place
        self.dates_tournament = dates_tournament
        self.time_control = time_control
        self.tournament_description = tournament_description
        self.tournament_rounds = []
        self.tournament_players = []
        self.tournament_scores = []


    def add_player(self, player):
        self.tournament_players.append(player)

    def add_round(self, round_):
        self.tournament_rounds.append(round_)

    def update_tournament_scores(self, tournament_score):
        self.tournament_scores.append(tournament_score)
