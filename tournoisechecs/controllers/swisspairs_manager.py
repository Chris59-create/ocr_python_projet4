class SwissPairs:
    """ appaire les joueurs pour le round1 avec les règles du tournoi suisse.
    Au début du premier tour, triez tous les joueurs en fonction de leur 
    classement.
    Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
    Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur
    joueur de la moitié inférieure, et ainsi de suite. Si nous avons huit 
    joueurs triés par rang, alors le joueur 1 est jumelé avec le joueur 5, 
    -le joueur 2 est jumelé avec le joueur 6, etc.
     """

    number_rounds = 1

    def pairs_players_round1(self):
        tournament_players_by_ranking = sorted(self.tournament_players, key=lambda x: x.rank, reverse=True)

        middle_index = len(tournament_players_by_ranking) // 2
        high_segment_players = tournament_players_by_ranking[:middle_index]
        low_segment_players = tournament_players_by_ranking[middle_index:]
        pairs_players = []

        for player_sup, player_inf in zip(high_segment_players, low_segment_players):
            pairs_players.append([player_sup, player_inf])

        print( "dans la fonction : ", pairs_players )

        return pairs_players

    def pairs_players_next_round(self):
        pass



    def choice_pairs_players_mode(self):

        if self.number_rounds == 1:
            pairs_players = self.pairs_players_round1()
        else:
            pairs_players = self.pairs_players_next_round()
        self.number_rounds += 1

        return pairs_players

    def run_creation_pairs_players(self, tournament_players):
        self.tournament_players = tournament_players
        pairs_players = self.choice_pairs_players_mode()

        return pairs_players

    