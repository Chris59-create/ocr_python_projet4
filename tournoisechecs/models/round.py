from datetime import datetime


class Round:
    def __init__(self, round_name, players_pairs):
        self.round_name = round_name
        self.players_pairs = players_pairs
        self.start_date_time = datetime.now()
        self.end_date_time = None
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def end_round(self):
        self.end_date_time = datetime.now()

    def update_score(self):
        pass
