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

    """Establish the list of all pairs of players who have played against each other during the current 
    tournament"""
    def list_all_played_pairs(self):
        self.played_pairs = []
        for round_ in self.tournament_rounds:
            for pairs_players in round_.pairs_players:
                self.played_pairs.append(pairs_players)

        print("toutes les paires jouées dans le tournoi : ", self.played_pairs)
        return self.played_pairs

    def search_opponent(self, players_by_score_rank, player):
        step = 1
        i = 0

        while i < len(players_by_score_rank):
            checker = 0

            next_player = players_by_score_rank[players_by_score_rank.index(player) + step]
            checker = self.check_opponent(self.played_pairs, player, next_player)

            if checker == 0:
                pair = [player, next_player]
                i = len(players_by_score_rank)
            else:
                step += 1
                i += 1

        return pair

    def check_opponent(self, played_pairs, player, next_player):
        checker = 0

        for pair in played_pairs:

            """print("to check : ", "player", player.last_name, "next player : ", next_player.last_name)
            print("checked : ", pair[0].last_name, "/", pair[1].last_name)"""

            result = all(element in pair for element in [player, next_player])
            """print(result)"""

            if result == True:
                checker += 1
            else:
                checker += 0

        """print("checker in check", checker)"""

        return checker

    def calculate_pairs_players_round1(self):

        pairs_players = []

        tournament_players_by_ranking = sorted(self.tournament_players, key=lambda x: x.rank, reverse=True)

        middle_index = len(tournament_players_by_ranking) // 2
        high_segment_players = tournament_players_by_ranking[:middle_index]
        low_segment_players = tournament_players_by_ranking[middle_index:]


        for player_sup, player_inf in zip(high_segment_players, low_segment_players):
            pair = [player_sup, player_inf]
            pairs_players.append(pair)

        print( "dans la fonction : ", pairs_players )

        return pairs_players

    def calculate_pairs_players_next_round(self):

        pairs_players = []

        players_by_score_rank = sorted(self.tournament_players, key=lambda x: (x.current_tournament_score, x.rank),
                                       reverse=True)
        played_pairs = self.list_all_played_pairs()

        while players_by_score_rank:
            #print("after while players_by_score_rank", players_by_score_rank)
            player = players_by_score_rank[0]

            pair = self.search_opponent(players_by_score_rank, player)
            pairs_players.append(pair)
            """for pair in pairs_players:
                print(pair[0].last_name, "/", pair[1].last_name)"""

            players_by_score_rank.remove(player)
            players_by_score_rank.remove(pair[1])
            #print(players_by_score_rank)





        return pairs_players





    def choice_pairs_players_mode(self , number_rounds):

        if number_rounds == 1:
            pairs_players = self.calculate_pairs_players_round1()
        else:
            pairs_players = self.calculate_pairs_players_next_round()

        return pairs_players

    def run_creation_pairs_players(self, tournament_players, tournament_rounds, number_rounds):
        self.tournament_players = tournament_players
        self.tournament_rounds = tournament_rounds
        pairs_players = self.choice_pairs_players_mode(number_rounds)

        return pairs_players

    