class Tournament:

    def __init__(self, tournament_name, place, dates_tournament, time_control, tournament_description="",
                 tournament_rounds=None, tournament_players=None, tournament_final_scores=None):
        self.tournament_name = tournament_name
        self.place = place
        self.dates_tournament = dates_tournament
        self.time_control = time_control
        self.tournament_description = tournament_description
        self.tournament_rounds = tournament_rounds or []
        self.tournament_players = tournament_players or []
        self.tournament_final_scores = tournament_final_scores or []

    def add_player(self, player):
        self.tournament_players.append(player)

    def add_round(self, round_):
        self.tournament_rounds.append(round_)

    def update_tournament_final_scores(self, tournament_score):
        self.tournament_final_scores.append(tournament_score)

    def __str__(self):
        return f"Nom du tournoi : {self.tournament_name} - Lieu : {self.place} - Date(s) : {self.dates_tournament}, " \
               f"Contrôle temps : {self.time_control}.\n Description : {self.tournament_description}\n"
