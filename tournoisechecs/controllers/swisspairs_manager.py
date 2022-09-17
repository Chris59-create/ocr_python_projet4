class SwissPairs:
    """ appaire les joueurs pour le round1 avec les règles du tournoi
    suisse.
    Au début du premier tour, triez tous les joueurs en fonction de leur
    classement.
    Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
    Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur
    joueur de la moitié inférieure, et ainsi de suite. Si nous avons huit
     joueurs triés par rang, alors le joueur 1 est jumelé avec le joueur 5,
     le joueur 2 est jumelé avec le joueur 6, etc."""

    """Establish the list of all pairs of players who have played
    against each other during the current tournament"""

    @staticmethod
    def list_all_played_pairs(tournament_rounds):

        played_pairs = []
        for round_ in tournament_rounds:
            for pairs_players in round_.pairs_players:
                played_pairs.append(pairs_players)

        # print("toutes les paires jouées dans le tournoi : ", "nombre : ", len(played_pairs))

        return played_pairs

    @staticmethod
    def check_opponent(player, next_player, played_pairs):

        checker = 0

        for pair in played_pairs:

            result = all(element in pair for element in [player, next_player])

            if result:
                checker += 1
            else:
                checker += 0

        return checker

    @staticmethod
    def reverse_check(new_1, new_2, played_pairs):

        for played_pair in played_pairs:

            result_new_1_pair1 = all(element in played_pair for element in new_1['new_pair1'])
            result_new_1_pair2 = all(element in played_pair for element in new_1['new_pair2'])
            result_new_2_pair3 = all(element in played_pair for element in new_2['new_pair3'])
            result_new_2_pair4 = all(element in played_pair for element in new_2['new_pair4'])

            if result_new_1_pair1 is False and result_new_1_pair2 is False:
                pairs = [new_1['new_pair1'], new_1['new_pair2']]
                break

            elif result_new_2_pair3 is False and result_new_2_pair4 is False:
                pairs = [new_2['new_pair3'], new_2['new_pair4']]
                break

            else:
                pairs = None

        return pairs

    def search_opponent(self, players_by_score_rank, player, future_pairs_players, played_pairs):

        pairs_to_add = None
        pair_to_del = []
        step = 1

        while not pairs_to_add:

            if (players_by_score_rank.index(player) + step) < len(players_by_score_rank):

                next_player = players_by_score_rank[players_by_score_rank.index(player) + step]
                checker = self.check_opponent(player, next_player, played_pairs)

                if checker == 0:
                    pairs_to_add = [[player, next_player]]

                else:
                    step += 1

            else:

                for pair_player in reversed(future_pairs_players):

                    player_to_reconsider_1 = pair_player[0]
                    available_player1 = players_by_score_rank[0]
                    player_to_reconsider_2 = pair_player[1]
                    available_player2 = players_by_score_rank[1]
                    new_1 = {'new_pair1': [player_to_reconsider_1, available_player1],
                             'new_pair2': [player_to_reconsider_2, available_player2]
                             }
                    new_2 = {'new_pair3': [player_to_reconsider_1, available_player2],
                             'new_pair4': [player_to_reconsider_2, available_player1]
                             }
                    pairs_to_add = self.reverse_check(new_1, new_2, played_pairs)

                    if pairs_to_add:
                        pair_to_del = [pair_player]
                        break

                    elif pair_player == reversed(future_pairs_players)[-1]:
                        next_player = players_by_score_rank[1]
                        pairs_to_add = [[player, next_player]]

        return pairs_to_add, pair_to_del

    @staticmethod
    def calculate_pairs_players_round1(tournament_players):

        pairs_players = []

        tournament_players_by_ranking = sorted(tournament_players, key=lambda x: x.rank, reverse=True)

        middle_index = len(tournament_players_by_ranking) // 2
        high_segment_players = tournament_players_by_ranking[:middle_index]
        low_segment_players = tournament_players_by_ranking[middle_index:]

        for player_sup, player_inf in zip(high_segment_players, low_segment_players):
            pair = [player_sup, player_inf]
            pairs_players.append(pair)

        return pairs_players

    def calculate_pairs_players_next_round(self, tournament_players, tournament_rounds):

        future_pairs_players = []

        players_by_score_rank = sorted(tournament_players, key=lambda x: (x.current_tournament_score, x.rank),
                                       reverse=True)

        played_pairs = self.list_all_played_pairs(tournament_rounds)

        while players_by_score_rank:

            player = players_by_score_rank[0]

            pairs_to_add, pair_to_del = self.search_opponent(players_by_score_rank,
                                                             player,
                                                             future_pairs_players,
                                                             played_pairs
                                                             )
            future_pairs_players = future_pairs_players + pairs_to_add
            future_pairs_players = [pair for pair in future_pairs_players if pair not in pair_to_del]

            players_by_score_rank.remove(player)

            if len(pairs_to_add) == 1:
                players_by_score_rank.remove(pairs_to_add[0][1])

            else:
                break

        return future_pairs_players

    def run_creation_pairs_players(self, tournament_players, tournament_rounds, number_rounds):

        if number_rounds == 1:
            pairs_players = self.calculate_pairs_players_round1(tournament_players)
        else:
            pairs_players = self.calculate_pairs_players_next_round(tournament_players, tournament_rounds)

        return pairs_players
