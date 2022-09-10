from datetime import datetime


class Round:

    def __init__(self, round_name, pairs_players, start_date_time=None, end_date_time=None, matches=None):
        self.round_name = round_name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matches = matches or []
        self.pairs_players = pairs_players

    def start_round(self):
        self.start_date_time = datetime.now()

    def end_round(self):
        self.end_date_time = datetime.now()

    def add_match(self, match):
        self.matches.append(match)

    def __str__(self):
        return f"{self.round_name} : du {self.start_date_time.strftime('%d/%m/%Y, %H:%M:%S')}" \
               f" au {self.end_date_time.strftime('%d/%m/%Y, %H:%M:%S')}"
