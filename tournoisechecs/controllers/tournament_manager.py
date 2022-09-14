from controllers.player_manager import PlayerManager
from controllers.swisspairs_manager import SwissPairs
from models.match import Match
from models.round import Round
from models.tournament import Tournament
from views.view_round import ViewRound
from views.view_tournament import ViewTournament

NUMBER_TOURNAMENT_PLAYERS = 8
NUMBER_ROUNDS = 4


class TournamentManager:
    """Tournament controller"""

    tournaments_instances = []
    number_rounds = 1

    def __init__(self):
        self.view_tournament = ViewTournament(self.tournaments_instances)

    # Crée le tournoi
    def input_tournament_data(self):
        tournament_data = self.view_tournament.input_tournament_data()
        tournament = Tournament(tournament_data["tournament_name"],
                                tournament_data["place"],
                                tournament_data["dates_tournament"],
                                tournament_data["time_control"],
                                tournament_data["tournament_description"]
                                )
        self.tournaments_instances.append(tournament)

        return tournament

    # Affiche les infos du tournoi
    def display_tournament_data(self, tournament):

        self.view_tournament.display_tournament_data(tournament)

    # Ajoute la liste des joueurs au tournoi
    @staticmethod
    def tournament_add_players(tournament):
        player_manager = PlayerManager()

        number_players_added = 0
        while len(tournament.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player = player_manager.add_player()
            tournament.tournament_players.append(player)
            number_players_added += 1
            print("Nombre de joueurs ajoutés au tournoi : ", number_players_added)

    # Calcule les paires de joueurs pour le round
    def calculate_pairs(self, tournament):
        pairs = SwissPairs()
        pairs_players = pairs.run_creation_pairs_players(tournament.tournament_players,
                                                         tournament.tournament_rounds, self.number_rounds)
        return pairs_players

    def prepare_round(self, tournament):
        round_name = "Round " + str(self.number_rounds)

        pairs_players = self.calculate_pairs(tournament)
        view_round = ViewRound()
        view_round.display_pairs_round(pairs_players)

        self.number_rounds += 1

        return round_name, pairs_players

    @staticmethod
    def start_round(round_name, pairs_players):

        round_ = Round(round_name, pairs_players)
        round_.start_round()

        return round_

    @staticmethod
    def update_score(tournament, round_):

        view_round = ViewRound()
        round_.end_round()

        for pair_players in round_.pairs_players:
            player1 = pair_players[0]
            player2 = pair_players[1]
            score_player1, score_player2 = view_round.input_score(player1, player2)
            match = Match(player1, score_player1, player2, score_player2)

            player1.update_current_tournament_score(score_player1)
            player2.update_current_tournament_score(score_player2)

            round_.add_match(match.match_tuple)

        tournament.add_round(round_)

    def update_tournament_final_scores(self, tournament):

        remaining_rounds = NUMBER_ROUNDS - len(tournament.tournament_rounds)

        # ! Check if all rounds have been played before updating the tournament final scores
        if remaining_rounds == 0:
            for player in tournament.tournament_players:
                final_tournament_score = [player, player.current_tournament_score]
                tournament.tournament_final_scores.append(final_tournament_score)
                player.current_tournament_score = 0
        else:
            # view_tournament = ViewTournament()
            self.view_tournament.display_tournament_in_progress()

        return remaining_rounds

    @staticmethod
    def player_data(element, index_element):
        tournament_rank = index_element
        first_name = element[0].first_name
        last_name = element[0].last_name
        date_birth = element[0].date_birth
        rank = element[0].rank
        score = element[1]

        player_data = {"tournament_rank": tournament_rank,
                       "first_name": first_name,
                       "last_name": last_name,
                       "date_birth": date_birth,
                       "rank": rank,
                       "score": score
                       }

        return player_data

    def display_tournament_total_scores(self, tournament, remaining_rounds):

        self.view_tournament.display_remaining_rounds(remaining_rounds)
        tournament_final_scores_sorted = sorted(tournament.tournament_final_scores, key=lambda x: x[1],
                                                reverse=True)
        for element in tournament_final_scores_sorted:
            index_element = tournament_final_scores_sorted.index(element)
            player_data = self.player_data(element, index_element)
            self.view_tournament.display_tournament_total_scores(player_data)

        return tournament_final_scores_sorted

    def update_tournament_players_ranks(self, tournament_final_scores_sorted):

        # self.display_tournament_total_scores()

        for element in tournament_final_scores_sorted:
            index_element = tournament_final_scores_sorted.index(element)
            player_data = self.player_data(element, index_element)
            self.view_tournament.display_tournament_total_scores(player_data)
            new_rank = self.view_tournament.input_tournament_player_new_rank()
            element[0].rank = new_rank

    def select_tournament(self):

        tournament = self.view_tournament.tournament_selection(tournament_selection_data={},
                                                               tournaments_list=self.tournaments_instances,
                                                               )

        if tournament is None:
            pass
        else:
            return tournament

    def display_tournament(self, tournament):

        self.view_tournament.display_tournament(tournament)

    @staticmethod
    def display_rounds(tournament, round_name=None):
        view_round = ViewRound()

        for round_ in tournament.tournament_rounds:

            matches_flat = [element for match in round_.matches for player_score in match for element in player_score]
            round_players = [matches_flat[index] for index in range(0, len(matches_flat), 2)]
            round_scores = [matches_flat[index] for index in range(1, len(matches_flat), 2)]
            round_results = dict(zip(round_players, round_scores))

            if round_name:

                if round_.round_name == round_name:
                    view_round.display_round(round_, round_results)

            else:

                view_round.display_round(round_, round_results)

    @staticmethod
    def display_matches(tournament):
        view_round = ViewRound()

        for round_ in tournament.tournament_rounds:

            for match in round_.matches:
                match_result = {}
                for player, score in match:
                    match_result[player] = score

                view_round.display_match(match_result)
