class Player:
    """Génère un joueur avec ses attributs et permet la modification
     de son classement"""

    def __init__(self, last_name, first_name, date_birth, gender, rank=0, current_tournament_score=0):
        self.last_name = last_name
        self.first_name = first_name
        self.date_birth = date_birth
        self.gender = gender
        self.rank = rank
        self.current_tournament_score = current_tournament_score

    def change_rank(self, new_rank):
        self.rank = new_rank

    def update_current_tournament_score(self, round_score):
        self.current_tournament_score += round_score

    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.gender}, né(e) le {self.date_birth} classé(e) {self.rank} "\
               f"- Score en cours : {self.current_tournament_score}"
