from itertools import combinations

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

        print("toutes les paires jouées dans le tournoi : ", "nombre : ", len(self.played_pairs))
        return self.played_pairs

    def search_opponent(self, players_by_score_rank, player):
        step = 1
        i = 0

        while i < len(players_by_score_rank):
            print(f"beginning  while i search component, len(players_by_score_rank : {len(players_by_score_rank)}")
            checker = 0

            print(players_by_score_rank.index(player))

            if players_by_score_rank.index(player) + step < len(players_by_score_rank):
                next_player = players_by_score_rank[players_by_score_rank.index(player) + step]
                checker = self.check_opponent(self.played_pairs, player, next_player)

                if checker == 0:
                    pair = [player, next_player]
                    i = len(players_by_score_rank)
                    print(f"In search_opponent i : {i} if checker == 0: ")
                else:
                    step += 1
                    i += 1
                    print(f"In search_opponent i : {i} if checker != 0: ")
            else:
                print("method for pairing the player, because following the main swiss rule he already played against "
                      "the last player available.Thus we will in this case chek the remaining not played pairs "
                      "possible for the player and do the same for the next_player")

                not_available_pairs = self.played_pairs + self.pairs_players
                all_pairs = []
                for element in self.theoretical_combinations_players:
                    list_element = list(element)
                    all_pairs.append(list_element)


                print("not_available_pairs : ", len(not_available_pairs))
                print("not_available_pairs : ", not_available_pairs)
                available_pairs = [pair for pair in all_pairs if pair not in
                                   not_available_pairs]
                print("available pairs : ", len(available_pairs))
                for_player_available_players = []

                for pair in available_pairs:
                    pair_list = list(pair)
                    if player in pair_list:
                        pair_list.remove(player)
                        available_player = pair_list[0]
                        for_player_available_players.append(available_player)

                available_players_by_score_rank = sorted(for_player_available_players, key=lambda x: (
                    x.current_tournament_score, x.rank))
                print("nombre de joueurs encore disponible", len(available_players_by_score_rank))
                pair = [player, available_players_by_score_rank[0]]
                print(f"\n Choosen available pair : {pair}")
                stop = input("wait an input to allow check previous process")
        print("In search_opponent, step : ", step, "player_index : ", players_by_score_rank.index(player))

        return pair

    def check_opponent(self, played_pairs, player, next_player):
        checker = 0

        for pair in played_pairs:

            """print("to check : ", "player", player.last_name, "next player : ", next_player.last_name)
            print("checked : ", pair[0].last_name, "/", pair[1].last_name)"""

            result = all(element in pair for element in [player, next_player])

            # test à supprimer
            print(f"pair joué : {pair[0].last_name} {pair[1].last_name} ")

            if result == True:
                checker += 1
            else:
                checker += 0

        # test à supprimer
        if checker != 0:
            print(f"check_opponent {player.last_name}, {next_player.last_name}")


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

        self.pairs_players = []

        players_by_score_rank = sorted(self.tournament_players, key=lambda x: (x.current_tournament_score, x.rank),
                                       reverse=True)
        self.theoretical_combinations_players = [i for i in combinations(self.tournament_players, 2)]
        print("theoretical combinations : ", self.theoretical_combinations_players)
        print(len(self.theoretical_combinations_players))

        self.list_all_played_pairs()

        while players_by_score_rank:
            #print("after while players_by_score_rank", players_by_score_rank)
            player = players_by_score_rank[0]

            pair = self.search_opponent(players_by_score_rank, player)
            self.pairs_players.append(pair)
            """for pair in pairs_players:
                print(pair[0].last_name, "/", pair[1].last_name)"""

            players_by_score_rank.remove(player)
            players_by_score_rank.remove(pair[1])
            print("check boucle calculate pairs next round", len(players_by_score_rank))





        return self.pairs_players





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

    