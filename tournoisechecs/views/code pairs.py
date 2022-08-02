




objects_players_by_ranking = sorted(tournoi1.tournament_players, key=lambda x: x.rank, reverse=True)

middle_index = len(objects_players_by_ranking) // 2

high_segment_players = objects_players_by_ranking[:middle_index]
low_segment_players = objects_players_by_ranking[middle_index:]
round1_pairs = []
round1_ranks_pairs = []
for player_sup, player_inf in zip(high_segment_players, low_segment_players):
    round1_pairs.append([player_sup, player_inf])
    round1_ranks_pairs.append([high_segment_players[high_segment_players.index(player_sup)].rank, low_segment_players[
        low_segment_players.index(player_inf)].rank])

players_ranks_by_rank = [objects_players_by_ranking[i].rank for i in range(8)]

high_ranks = [high_segment_players[i].rank for i in range(4)]
low_ranks = [low_segment_players[i].rank for i in range(4)]

print("segment sup : ", high_ranks)
print("segment inf : ", low_ranks)
print(round1_pairs)
print(round1_ranks_pairs)
