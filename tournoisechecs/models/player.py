import itertools

class Player:
    """Génère un joueur avec ses attributs et permet la modification
     de son classement"""
    new_id = itertools.count(1)
    players_instances = []

    def __init__(self, last_name, first_name, date_birth, gender, rank=0):

        self.last_name = last_name
        self.first_name = first_name
        self.date_birth = date_birth
        self.gender = gender
        self.rank = rank
        self.__class__.players_instances.append(self)
        self.current_tournament_score = 0
        self.player_id = "to built"

    def change_rank(self, new_rank):
        self.rank = new_rank

    def update_current_tournament_score(self, round_score):
        self.current_tournament_score += round_score