import pyinputplus as pypi

class UpdateScores:


    def display_pair_players(self, pair_players):
        self.pair_players = pair_players
        print(self.pair_players)

    def update_scores(self, pair_players):
        self.pair_players = pair_players
        self.pair_scores = []
        for player in self.pair_players:
            print(f"Entrez le score de {player.last_name} : ")
            score = float(pypi.inputMenu(["0", "0.5", "1"], lettered=True))
            self.pair_scores.append(score)

        return self.pair_scores
