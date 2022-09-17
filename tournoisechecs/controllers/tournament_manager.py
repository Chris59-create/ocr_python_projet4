from colorama import init, Fore, Back

from controllers.player_manager import PlayerManager
from controllers.swisspairs_manager import SwissPairs
from models.match import Match
from models.round import Round
from models.tournament import Tournament
from views.view_round import ViewRound
from views.view_tournament import ViewTournament

init()

NUMBER_TOURNAMENT_PLAYERS = 8
NUMBER_ROUNDS = 4


class TournamentManager:
    """
    Contains all the methods needed to manage step by step a tournament.
    Class variables:
    - tournaments_instances: an empty list to store the future tournaments.
    - number_rounds:    initialize to 1 this variable which will be
                        incremented during a tournament process.
    """

    tournaments_instances = []
    number_rounds = 1

    def __init__(self):
        """Instantiated view_tournament to allow use of the methods of
        ViewTournament (module view_tournament) needed to input and
        display data of a tournament"""
        self.view_tournament = ViewTournament(self.tournaments_instances)

    # Crée le tournoi
    def input_tournament_data(self):
        """Calls the method needed to enter the tournament features,
        create the tournament as object of the class Tournament (module
        tournament in models), add it to list of tournaments. Returns the
        object tournament """

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

    @staticmethod
    def tournament_add_players(tournament):
        """calls the needed times to have the number of players required
        for a tournament the method to select or create a player. Add it
        to the list of players of the tournament"""

        player_manager = PlayerManager()

        number_players_added = 0
        while len(tournament.tournament_players) < NUMBER_TOURNAMENT_PLAYERS:
            player = player_manager.add_player()

            if not player:
                pass

            else:

                tournament.tournament_players.append(player)
                number_players_added += 1

                print(Back.BLACK)
                print(Fore.BLUE+"Nombre de joueurs ajoutés au tournoi : ", number_players_added)

    def calculate_pairs(self, tournament):
        """Called by self prepare_round(), return the list of the pairs
        of players who will play one against the other during the round.
        Passes the list of players, the list of played rounds and the
        number of the round concerned to the method which will return the
        list of pairs"""

        pairs = SwissPairs()
        pairs_players = pairs.run_creation_pairs_players(tournament.tournament_players,
                                                         tournament.tournament_rounds, self.number_rounds)

        return pairs_players

    def prepare_round(self, tournament):
        """Calls the method which will determine the players who will
        play one against the other, increments the number of rounds."""
        round_name = "Round " + str(self.number_rounds)

        pairs_players = self.calculate_pairs(tournament)
        view_round = ViewRound()
        view_round.display_pairs_round(pairs_players)

        self.number_rounds += 1

        return round_name, pairs_players

    @staticmethod
    def start_round(round_name, pairs_players):
        """Create the object round_ in class Round (module round in
        models and call the method of this class to register the start
        date and time of the round"""

        round_ = Round(round_name, pairs_players)
        round_.start_round()

        return round_

    @staticmethod
    def update_score(tournament, round_):
        """Calls the method to register date and time of the end of the
        round. Pairs of players by pairs of player calls the method to
        update their scores, create the object match in the class Match
        (module match in models) and update the attribute current
        tournament score of the players (used to calculate later the final
        scores of tournament). Calls the method to add the match to the
        round. Calls the method to add the round to the tournament.
        """

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
        """ Checks if all rounds of the tournaments have been played and
        when calls the method to add the player and his final score to
        tournament_final_scores of the tournament. If this method is
        called before end of the tournament, it calls the display of a
        warning."""

        remaining_rounds = NUMBER_ROUNDS - len(tournament.tournament_rounds)

        if remaining_rounds == 0:

            for player in tournament.tournament_players:
                final_tournament_score = [player, player.current_tournament_score]
                tournament.tournament_final_scores.append(final_tournament_score)
                player.current_tournament_score = 0
        else:

            self.view_tournament.display_tournament_in_progress()

        return remaining_rounds

    @staticmethod
    def player_data(element, index_element):
        """Called by the self method display_tournament_total_scores.
        Returns a dict of data useful to display the final scores"""

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
        """Called by a method of the class MenuTournament (module view_menus
        in views) iterate in the list of final scores sorted par score
        and calls the method to display in order the element of the list"""

        self.view_tournament.display_remaining_rounds(remaining_rounds)
        tournament_final_scores_sorted = sorted(tournament.tournament_final_scores, key=lambda x: x[1],
                                                reverse=True)
        for element in tournament_final_scores_sorted:
            index_element = tournament_final_scores_sorted.index(element)
            player_data = self.player_data(element, index_element)
            self.view_tournament.display_tournament_total_scores(player_data)

        return tournament_final_scores_sorted

    def update_tournament_players_ranks(self, tournament_final_scores_sorted):
        """Called by a method of the class MenuTournament (module view_menus
        in views) iterate in the list of final scores sorted par score
        and calls each time the method to enter a new rank, uses the new
        rank value to update the rank of the relative player."""

        for element in tournament_final_scores_sorted:
            index_element = tournament_final_scores_sorted.index(element)
            player_data = self.player_data(element, index_element)
            self.view_tournament.display_tournament_total_scores(player_data)
            new_rank = self.view_tournament.input_tournament_player_new_rank()
            element[0].rank = new_rank

    def select_tournament(self):
        """Called by methods of MenuReports (module view_menus in views)
        call the method to select a tournament and return the selected
        tournament."""

        tournament = self.view_tournament.tournament_selection(tournament_selection_data={},
                                                               tournaments_list=self.tournaments_instances,
                                                               )

        if tournament is None:
            pass

        else:
            return tournament

    def display_tournament(self, tournament):
        """Called by  a method of MenuReports (module view_menus in views)
        call the method to display a tournament."""

        self.view_tournament.display_tournament(tournament)

    @staticmethod
    def display_rounds(tournament, round_name=None):
        """Called by methods of MenuReports (module view_menus in views)
        unpacks the matches(tuples of two lists) to create a flat list
        (without nested lists) with the data. Uses this flat list to build
        a list of players and a list of scores. Matchs the two lists to
        build a dict (Keys = players, values = scores. The if statement
        allows to use these method if called for a specific round or else
        if called without specific round, meant for all rounds of the
        tournament"""

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
        """Called by  a method of MenuReports (module view_menus in views)
        Iterates through the rounds and their matches to display all
        matches of a tournament."""

        view_round = ViewRound()

        for round_ in tournament.tournament_rounds:

            for match in round_.matches:
                match_result = {}
                for player, score in match:
                    match_result[player] = score

                view_round.display_match(match_result)

    def display_tournament_players_sorted(self, tournament, criteria):
        """Called by a method of the class MenuReports (module view_menus
        in views) iterate in the list of final scores of tournament sorted
        by criteria and calls the method to display in order the element
        of the list with his final score in the tournament."""

        if criteria == "alphabetical":

            tournament_final_scores_sorted = sorted(tournament.tournament_final_scores,
                                                    key=lambda x: (x[0].last_name, x[0].first_name),
                                                    )

        elif criteria == "rank":

            tournament_final_scores_sorted = sorted(tournament.tournament_final_scores,
                                                    key=lambda x: x[0].rank,
                                                    reverse=True
                                                    )

        for element in tournament_final_scores_sorted:
            index_element = tournament_final_scores_sorted.index(element)
            player_data = self.player_data(element, index_element)
            self.view_tournament.display_tournament_total_scores(player_data)
