import pyinputplus as pyip
from datetime import datetime


class ViewTournament:

    @staticmethod
    def input_tournament_data():
        dates_tournament = []
        tournament_name = pyip.inputStr("\nNom du tournoi : ")
        place = pyip.inputStr("Lieu du tournoi : ")

        input_date = "yes"
        while input_date == "yes":
            date_tournament = pyip.inputDate("Date (jjmmaaaa) : ", formats=['%d%m%Y'])
            dates_tournament.append(datetime.strftime(date_tournament, '%d/%m/%Y'))
            input_date = pyip.inputYesNo(prompt="Voulez-vous ajouter une date au tournoi Oui (y/Y) / Non (n/N) : ")

        time_control = pyip.inputMenu(["Bullet", "Blitz", "Coup rapide"], numbered=True)
        tournament_description = pyip.inputStr("Description du tournoi : ", blank=True)

        return {"tournament_name": tournament_name,
                "place": place,
                "dates_tournament": dates_tournament,
                "time_control": time_control,
                "tournament_description": tournament_description
                }

    @staticmethod
    def display_tournament_data(tournament):

        print()
        print(f"Vous avez créé un tournoi avec les informations suivantes :\n \n"
              f"Nom du tournoi : {tournament.tournament_name}\n"
              f"Lieu du tournoi : {tournament.place}\n"
              f"Date(s) : {tournament.dates_tournament}\n"
              f"Contrôle du temps : {tournament.time_control}\n"
              f"Description : {tournament.tournament_description}")
        print()

    @staticmethod
    def display_tournament_in_progress():  # Vérifier si pas inutile
        print("\nCette action n'est pas possible tant que le tournoi n'est pas terminé !\n")

    @staticmethod
    def display_remaining_rounds(remaining_rounds):
        print(f"Il reste {remaining_rounds} tour(s) à jouer pour ce tournoi.\n")

    @staticmethod
    def display_tournament_total_scores(player_data):
        tournament_rank = player_data["tournament_rank"]
        first_name = player_data["first_name"]
        last_name = player_data["last_name"]
        date_birth = player_data["date_birth"]
        rank = player_data["rank"]
        score = player_data["score"]

        print(f"{tournament_rank+1}. {first_name} {last_name} né(e) le {date_birth} classé(e) {rank} - Score : "
              f"{score}")

    @staticmethod
    def input_tournament_player_new_rank():

        new_rank = pyip.inputInt(prompt="Saisir le nouveau classement du joueur : \n")

        return new_rank

    def display_all_players_by_rank(self):
        pass
