from tinydb import TinyDB

from controllers.tournament_manager import TournamentManager

db = TinyDB('db.json')
tournaments_table = db.table("tournaments")

class TableTournament:

    def __init__(self):
        self.tournament_manager = TournamentManager()

    def save_tournaments_data(self):

        tournaments_table.truncate()

        serialized_tournaments = []
        for tournament in self.tournament_manager.tournaments_instances:

            # serialization round - match
            serialized_rounds = []
            for round_ in tournament.tournament_rounds:

                serialized_matches = []
                for match in round_.matches:

                    serialized_match = []
                    for player, score in match:
                        date_birth_str = player.date_birth.strftime('%d%m%Y')
                        serialized_match_player = {
                            'player lastname': player.last_name,
                            'player firstname': player.first_name,
                            'player date birth': date_birth_str,
                            'player gender': player.gender,
                            'score player': score,
                        }

                        serialized_match.append(serialized_match_player)

                    serialized_matches.append(serialized_match)

                print("test serialized_matches", serialized_matches)

                serialized_pairs_players = []
                for pair_players in round_.pairs_players:
                    date_birth_str_1 = pair_players[0].date_birth.strftime('%d%m%Y')
                    date_birth_str_2 = pair_players[1].date_birth.strftime('%d%m%Y')
                    serialized_pair_players = {
                        'last_name1': pair_players[0].last_name,
                        'first_name1': pair_players[0].first_name,
                        'date_birth1': date_birth_str_1,
                        'gender1': pair_players[0].gender,
                        'rank1': pair_players[0].rank,
                        'current_tournament_score1': pair_players[0].current_tournament_score,
                        'player_id1': pair_players[0].player_id,
                        'last_name2': pair_players[1].last_name,
                        'first_name2': pair_players[1].first_name,
                        'date_birth2': date_birth_str_2,
                        'gender2': pair_players[1].gender,
                        'rank2': pair_players[1].rank,
                        'current_tournament_score2': pair_players[1].current_tournament_score,
                        'player_id2': pair_players[1].player_id
                    }

                    serialized_pairs_players.append(serialized_pair_players)

                print("test serialized_pairs_players", serialized_pairs_players)

                serialized_round = {
                    'round_name': round_.round_name,
                    'start_date_time': round_.start_date_time.strftime('%d%m%Y %H:%M:%S'),
                    'end_date_time': round_.end_date_time.strftime('%d%m%Y %H:%M:%S'),
                    'matches': serialized_matches,
                    'pairs_players': serialized_pairs_players
                }

                serialized_rounds.append(serialized_round)

            print("test serialized_rounds", serialized_rounds)

            # serialization de la liste des joueurs
            serialized_tournament_players = []
            for player in tournament.tournament_players:
                date_birth_str = player.date_birth.strftime('%d%m%Y')
                serialized_player = {
                    'last_name': player.last_name,
                    'first_name': player.first_name,
                    'date_birth': date_birth_str,
                    'gender': player.gender,
                    'rank': player.rank,
                    'current_tournament_score': player.current_tournament_score,
                    'player_id': player.player_id
                }

                serialized_tournament_players.append(serialized_player)

            print("test serialized_tournament_players", serialized_tournament_players)

            # serialisation de la liste des scores
            serialized_tournament_final_scores = []
            for player, final_score in tournament.tournament_final_scores:
                date_birth_str = player.date_birth.strftime('%d%m%Y')
                serialized_final_score = {
                    'last_name': player.last_name,
                    'first_name': player.first_name,
                    'date_birth': date_birth_str,
                    'gender': player.gender,
                    'rank': player.rank,
                    'current_tournament_score': player.current_tournament_score,
                    'player_id': player.player_id,
                    'final_score': final_score
                }

                serialized_tournament_final_scores.append(serialized_final_score)

            print("test serialized_tournament_final_scores", serialized_tournament_final_scores)

            # serialization de tout le tournoi
            serialized_tournament = {
                'tournament name': tournament.tournament_name,
                'place': tournament.place,
                'dates tournament': tournament.dates_tournament,
                'time control': tournament.time_control,
                'tournament description': tournament.tournament_description,
                'tournament rounds': serialized_rounds,
                'tournament players': serialized_tournament_players,
                'tournament final scores': serialized_tournament_final_scores
            }

            serialized_tournaments.append(serialized_tournament)

        print("test serialized tournaments", serialized_tournaments)
        tournaments_table.insert_multiple(serialized_tournaments)
