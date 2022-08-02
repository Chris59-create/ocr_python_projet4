from datetime import datetime

class Round:

    def __init__(self, round_name, pairs_players):
        self.round_name = round_name
        self.start_date_time = datetime.now()
        self.end_date_time = None
        self.matches = []
        self.pairs_players = pairs_players

    def display_pairs_players(self):
        pass

    def end_round(self):
        self.end_date_time = datetime.now()


    def add_match(self, match ):
        self.matches.append(match)



