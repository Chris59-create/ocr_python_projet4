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

    def search_opponent(self, players_by_score_rank, player, future_pairs_players, played_pairs):
        step = 1
        i = 0

        while i < len(players_by_score_rank):
            # print(f"beginning  while i search component, len(players_by_score_rank : {len(players_by_score_rank)}")
            checker = 0

            # print("index player in players_by_score_rank : ", players_by_score_rank.index(player))

            if players_by_score_rank.index(player) + step < len(players_by_score_rank):
                next_player = players_by_score_rank[players_by_score_rank.index(player) + step]
                checker = self.check_opponent(player, next_player, played_pairs)

                if checker == 0:
                    pair = [player, next_player]
                    i = len(players_by_score_rank)
                    # print(f"In search_opponent i : {i} if checker == 0: ")
                    # stop = input("pause to check the process checker == 0") #à supprimer
                else:
                    step += 1
                    i += 1

                    # print(f"In search_opponent i : {i} if checker != 0: ")
                    # stop = input("pause to check the process") #à supprimer
            else:
                reverse = 1

                for pair_player in reversed(future_pairs_players):
                    # print("tentative reverse : ", reverse)

                    # print("played_pairs : ", len(played_pairs))

                    if played_pairs:

                        # stop = input("Pause to check the process after played_pairs True") #à supprimer

                        # print("reversed list : ", reversed(future_pairs_players)) #à supprimer
                        # print("pair_player dans 1er for", pair_player) #à supprimer

                        player_to_reconsider_1 = pair_player[0]
                        available_player1 = players_by_score_rank[0]
                        player_to_reconsider_2 = pair_player[1]
                        available_player2 = players_by_score_rank[1]
                        new_pair1 = [player_to_reconsider_1,  available_player1]
                        new_pair2 = [player_to_reconsider_2, available_player2]

                        t = 1  # à supprimer
                        for played_pair in played_pairs:

                            # print("tentative : ", t)

                            """print("to check : ", "player", player.last_name, "next player : ",
                            next_player.last_name)
                            print("checked : ", pair[0].last_name, "/", pair[1].last_name)"""  # à supprimer

                            result_new_pair1 = all(element in played_pair for element in new_pair1)
                            result_new_pair2 = all(element in played_pair for element in new_pair2)

                            if result_new_pair1 is False and result_new_pair2 is False:
                                # print("pair_player dans if avant remove1", pair_player) #à supprimer
                                played_pairs.remove(played_pair)
                                pair = new_pair1
                                # print("new_pair ok)") #à supprimer
                                # stop = input("pause to check the process") # à supprimer
                            else:
                                t += 1

                        reverse += 1

                    else:
                        pair = [pair_player[0], pair_player[1]]

        return pair

    @staticmethod
    def check_opponent(player, next_player, played_pairs):

        checker = 0

        for pair in played_pairs:

            # print("to check : ", "player", player.last_name, "next player : ", next_player.last_name)
            # print("checked : ", pair[0].last_name, "/", pair[1].last_name)
            result = all(element in pair for element in [player, next_player])

            # test à supprimer
            # print(f"pair joué : {pair[0].last_name} {pair[1].last_name} ")

            if result:
                checker += 1
            else:
                checker += 0

        # test à supprimer

        # if checker != 0:
            # print(f"check_opponent {player.last_name}, {next_player.last_name}")

        return checker

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

        # print( "dans la fonction : ", pairs_players )

        return pairs_players

    def calculate_pairs_players_next_round(self, tournament_players, tournament_rounds):

        future_pairs_players = []

        players_by_score_rank = sorted(tournament_players, key=lambda x: (x.current_tournament_score, x.rank),
                                       reverse=True)

        played_pairs = self.list_all_played_pairs(tournament_rounds)

        while players_by_score_rank:
            # print("after while players_by_score_rank", players_by_score_rank)
            player = players_by_score_rank[0]

            pair = self.search_opponent(players_by_score_rank, player, future_pairs_players, played_pairs)
            future_pairs_players.append(pair)

            players_by_score_rank.remove(player)
            players_by_score_rank.remove(pair[1])
            # print("check boucle calculate pairs next round", len(players_by_score_rank))

        return future_pairs_players

    def choice_pairs_players_mode(self, number_rounds, tournament_players, tournament_rounds):

        if number_rounds == 1:
            pairs_players = self.calculate_pairs_players_round1(tournament_players)
        else:
            pairs_players = self.calculate_pairs_players_next_round(tournament_players, tournament_rounds)

        return pairs_players

    def run_creation_pairs_players(self, tournament_players, tournament_rounds, number_rounds):

        pairs_players = self.choice_pairs_players_mode(number_rounds, tournament_players, tournament_rounds)

        return pairs_players
