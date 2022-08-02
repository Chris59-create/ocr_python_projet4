
NUMBER_ROUNDS = 4
ROUNDS_NAMES = [f"round{i}" for i in range(1, NUMBER_ROUNDS+1)]

class Tournament:
    def __init__(self, tournament_name, place, dates_tournament, time_control, tournament_description=""):
        self.tournament_name = tournament_name
        self.place = place
        self.dates_tournament = dates_tournament
        self.time_control = time_control
        self.tournament_description = tournament_description
        self.rounds = []
        self.tournament_players = []


    def add_player(self, player):
        self.tournament_players.append(player)

    def add_round(self, round_):
        self.rounds.append(round_)

class TournamentScore(Tournament):

    def __init__(self, player, round_score):
        self.player = player
        self.round_score = round_score
        self.total_score = 0
        self.tournament_total_scores = []


    def totalize_score(self):
        self.total_score += self.round_score