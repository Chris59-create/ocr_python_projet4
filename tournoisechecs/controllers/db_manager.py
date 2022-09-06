from datetime import datetime

from controllers.player_manager import PlayerManager
from controllers.tournament_manager import TournamentManager
from models.match import Match
from models.player import Player
from models.round import Round
from models.tournament import Tournament
from tinydb import TinyDB

db = TinyDB('db.json')
tournaments_table = db.table("tournaments")
players_table = db.table("players")


class TableTournament:

    def __init__(self):
        self.tournament_manager = TournamentManager()
        self.table_player = TablePlayers()

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

                    print("test", match)

                    for player, score in match:
                        serialized_player = self.table_player.serialize_player(player)
                        serialized_match_player = {'serialized_player': serialized_player, 'score player': score}

                        serialized_match.append(serialized_match_player)

                    serialized_matches.append(serialized_match)

                print("\ntest serialized_matches\n", serialized_matches)

                serialized_pairs_players = []
                for pair_players in round_.pairs_players:
                    serialized_player_0 = self.table_player.serialize_player(pair_players[0])
                    serialized_player_1 = self.table_player.serialize_player(pair_players[1])
                    serialized_pair_players = {'serialized_player_0': serialized_player_0,
                                               'serialized_player_1': serialized_player_1
                                               }
                    serialized_pairs_players.append(serialized_pair_players)

                print("test serialized_pairs_players", serialized_pairs_players)

                serialized_round = {
                    'round_name': round_.round_name,
                    'start_date_time': round_.start_date_time.strftime('%d%m%Y, %H:%M:%S'),
                    'end_date_time': round_.end_date_time.strftime('%d%m%Y, %H:%M:%S'),
                    'matches': serialized_matches,
                    'pairs_players': serialized_pairs_players
                }

                serialized_rounds.append(serialized_round)

            print("test serialized_rounds", serialized_rounds)

            # serialization de la liste des joueurs
            serialized_tournament_players = []
            for player in tournament.tournament_players:
                serialized_player = self.table_player.serialize_player(player)
                serialized_tournament_players.append(serialized_player)

            print("test serialized_tournament_players", serialized_tournament_players)

            # serialisation de la liste des scores
            serialized_tournament_final_scores = []
            for player, final_score in tournament.tournament_final_scores:
                serialized_player = self.table_player.serialize_player(player)
                serialized_final_score = {'player': serialized_player, 'final_score': final_score}

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

    def install_tournament_data(self):

        serialized_tournaments = tournaments_table.all()

        # Deserialization of tournaments
        for serialized_tournament in serialized_tournaments:

            # Deserialization of tournament rounds
            serialized_tournament_rounds = serialized_tournament['tournament rounds']

            deserialized_rounds = []
            for serialized_round in serialized_tournament_rounds:

                # Deserialization of matches
                deserialized_matches = []
                for serialized_match in serialized_round['matches']:

                    player_score_1 = serialized_match[0]
                    player_score_2 = serialized_match[1]

                    serialized_player_1 = player_score_1['serialized_player']
                    deserialized_player_1 = self.table_player.deserialize_player(serialized_player_1)
                    score_player_1 = player_score_1['score player']
                    serialized_player_2 = player_score_2['serialized_player']
                    deserialized_player_2 = self.table_player.deserialize_player(serialized_player_2)
                    score_player_2 = player_score_2['score player']

                    deserialized_match = Match(deserialized_player_1,
                                               score_player_1,
                                               deserialized_player_2,
                                               score_player_2
                                               )

                    deserialized_matches.append(deserialized_match.match_tuple)

                # Deserialization of pair players
                deserialized_pairs_players = []
                for serialized_pair_players in serialized_round['pairs_players']:

                    deserialized_player_0 = self.table_player.deserialize_player(
                        serialized_pair_players['serialized_player_0']
                    )
                    deserialized_player_1 = self.table_player.deserialize_player(
                        serialized_pair_players['serialized_player_1']
                    )
                    deserialized_pair_players = [deserialized_player_0, deserialized_player_1]

                    deserialized_pairs_players.append(deserialized_pair_players)

                deserialized_round = Round(serialized_round['round_name'],
                                           deserialized_pairs_players,
                                           serialized_round['start_date_time'],
                                           serialized_round['end_date_time'],
                                           deserialized_matches
                                           )

                deserialized_rounds.append(deserialized_round)

            # Deserialization of tournament players
            deserialized_tournament_players = []
            for serialized_player in serialized_tournament['tournament players']:
                deserialized_player = self.table_player.deserialize_player(serialized_player)

                deserialized_tournament_players.append(deserialized_player)

            # Deserialization of tournament final scores
            deserialized_tournament_final_scores = []
            for serialized_tournament_final_score in serialized_tournament['tournament final scores']:
                serialized_player = serialized_tournament_final_score['player']
                deserialized_player = self.table_player.deserialize_player(serialized_player)
                deserialized_final_score = serialized_tournament_final_score['final_score']
                deserialized_tournament_final_score = [deserialized_player, deserialized_final_score]

                deserialized_tournament_final_scores.append(deserialized_tournament_final_score)

            # Deserialization of all tournament
            deserialized_tournament = Tournament(
                serialized_tournament['tournament name'],
                serialized_tournament['place'],
                serialized_tournament['dates tournament'],
                serialized_tournament['time control'],
                serialized_tournament['tournament description'],
                deserialized_rounds,
                deserialized_tournament_players,
                deserialized_tournament_final_scores
            )

            self.tournament_manager.tournaments_instances.append(deserialized_tournament)


class TablePlayers:

    def __init__(self):

        self.player_manager = PlayerManager()

    def serialize_player(self, player):

        date_birth_str = player.date_birth.strftime('%d%m%Y')
        serialized_player = {'last_name': player.last_name,
                             'first_name': player.first_name,
                             'date_birth': date_birth_str,
                             'gender': player.gender,
                             'rank': player.rank,
                             'current_tournament_score': player.current_tournament_score
                             }

        return serialized_player

    def deserialize_player(self, serialized_player):

        date_birth = datetime.strptime(serialized_player['date_birth'], '%d%m%Y')
        player = Player(serialized_player['last_name'],
                        serialized_player['first_name'],
                        date_birth,
                        serialized_player['gender'],
                        serialized_player['rank'],
                        serialized_player['current_tournament_score']
                        )

        return player

    def save_players_data(self):

        players_table.truncate()
        serialized_players = []
        for player in self.player_manager.players_instances:
            serialized_player = self.serialize_player(player)
            serialized_players.append(serialized_player)

        players_table.insert_multiple(serialized_players)

    def install_players_data(self):

        serialized_players = players_table.all()
        for serialized_player in serialized_players:
            deserialized_player = self.deserialize_player(serialized_player)
            self.player_manager.players_instances.append(deserialized_player)
