class Match:

    def __init__(self, player1, score_player1, player2, score_player2):
        self.player1 = player1
        self.score_player1 = score_player1
        self.player2 = player2
        self.score_player2 = score_player2
        self.match_tuple = ([self.player1, score_player1], [self.player2, self.score_player2])

    def __str__(self):
        return f"{self.match_tuple}"
