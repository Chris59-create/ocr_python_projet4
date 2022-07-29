# Create un new tournament
# Add 8 players
    # App generates pairs of players for the first round
    # App generate round and matches
# Enter the results of the first round
# Repeat for the next '"rounds the following steps : pairs / results
from tests.testtournament import test_instance, tournoi1
from tournoisechecs.models.tournament import Tournament
from tournoisechecs.models.player import Player

""" appaire les joueurs pour le round1 avec les règles du tournoi suisse.
Au début du premier tour, triez tous les joueurs en fonction de leur 
classement.
Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur
joueur de la moitié inférieure, et ainsi de suite. Si nous avons huit 
joueurs triés par rang, alors le joueur 1 est jumelé avec le joueur 5, 
-le joueur 2 est jumelé avec le joueur 6, etc.
 """
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
