import pyinputplus as pyip
from datetime import datetime


class ViewTournament:

    def test_tournament_data(self):
        return {"tournament_name": "tournoi test",
                "place": "Solbach",
                "dates_tournament": ["10/08/2022"],
                "time_control": "Bullet",
                "tournament_description": "blablabla"
                }

    def input_tournament_data(self):
        dates_tournament = []
        tournament_name = pyip.inputStr("Nom du tournoi : ")
        place = pyip.inputStr("Lieu du tournoi : ")

        input_date = True
        while input_date:
            date_tournament = pyip.inputDate("Date (jjmmaaaa) : ", formats=['%d%m%Y'])
            dates_tournament.append(datetime.strftime(date_tournament, '%d/%m/%Y'))
            input_date = pyip.inputBool("Voulez-vous ajouter une date au tournoi Oui = t Non = f: ", "True", "False")

        time_control = pyip.inputMenu(["Bullet", "Blitz", "Coup rapide"], numbered=True)
        tournament_description = pyip.inputStr("Description du tournoi : ", blank=True)

        return {"tournament_name": tournament_name,
                "place": place,
                "dates_tournament": dates_tournament,
                "time_control": time_control,
                "tournament_description": tournament_description
                }

    def display_tournament_data(self, tournament):
        self.tournament = tournament

        print()
        print(f"Vous avez créé un tournoi avec les informations suivantes :\n \n"
              f"Nom du tournoi : {self.tournament.tournament_name}\n"
              f"Lieu du tournoi : {self.tournament.place}\n"
              f"Date(s) : {self.tournament.dates_tournament}\n"
              f"Contrôle du temps : {self.tournament.time_control}\n"
              f"Description : {self.tournament.tournament_description}")
        print()

    def display_tournament_in_progress(self):  # Vérifier si pas inutile
        print("\nCette action n'est pas possible tant que le tournoi n'est pas terminé !\n")

    def display_remaining_rounds(self, remaining_rounds):
        print(f"Il reste {remaining_rounds} tour(s) à jouer pour ce tournoi.\n")

    def display_tournament_total_scores(self, player_data):
        tournament_rank = player_data["tournament_rank"]
        first_name = player_data["first_name"]
        last_name = player_data["last_name"]
        date_birth = player_data["date_birth"]
        rank = player_data["rank"]
        score = player_data["score"]

        print(f"{tournament_rank+1}. {first_name} {last_name} né(e) le {date_birth} classé(e) {rank} - Score : "
              f"{score}")

    def input_tournament_player_new_rank(self):
        print("test saisie nouveau classement")
        new_rank = pyip.inputInt(prompt="\nSaisir le nouveau classement du joueur : \n")

        return new_rank

    def display_all_players_by_rank(self):
        pass
