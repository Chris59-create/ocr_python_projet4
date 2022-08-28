from datetime import datetime


class Round:

    def __init__(self, round_name, pairs_players, start_date_time=datetime.now(), end_date_time=None, matches=[]):
        self.round_name = round_name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matches = matches
        self.pairs_players = pairs_players

    def display_pairs_players(self):
        pass

    def end_round(self):
        self.end_date_time = datetime.now()

    def add_match(self, match):
        self.matches.append(match)
