from tinydb import TinyDB
from datetime import datetime
from controllers.tournament_manager import TournamentManager
from controllers.player_manager import PlayerManager
from models.player import Player

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
                    for player, score in match:
                        serialized_player = self.table_player.serialize_player(player)
                        serialized_match_player = {'serialized_player': serialized_player, 'score player': score}
                            
                        serialized_match.append(serialized_match_player)

                    serialized_matches.append(serialized_match)

                print("test serialized_matches", serialized_matches)

                serialized_pairs_players = []
                for pair_players in round_.pairs_players:
                    serialized_player_O = self.table_player.serialize_player(pair_players[0])
                    serialized_player_1 = self.table_player.serialize_player(pair_players[1])
                    serialized_pair_players = {'serialized_player_O': serialized_player_O, 
                                               'serialized_player_1': serialized_player_1
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
        pass


class TablePlayers:

    def __init__(self):

        self.player_manager = PlayerManager()

    def serialize_player(self, player):
        
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
                
        return serialized_player

    def deserialize_player(self, serialized_player):

        date_birth = datetime.strptime(serialized_player['date_birth'], '%d%m%Y')
        player = Player(serialized_player['last_name'],
                        serialized_player['first_name'],
                        date_birth,
                        serialized_player['gender'],
                        serialized_player['rank'],
                        serialized_player['current_tournament_score'],
                        serialized_player['player_id'])

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
