class Player:
    """Génère un joueur avec ses attributs et permet la modification
     de son classement"""

    def __init__(self, last_name, first_name, date_birth, gender, rank):
        self.last_name = last_name
        self.first_name = first_name
        self.date_birth = date_birth
        self.gender = gender
        self.rank = rank

    def change_rank(self, new_rank):
        self.rank = new_rank