import pyinputplus as pyip
from datetime import datetime


class ViewTournament:

    def test_tournament_data(self):
        return "tournoi test", "Solbach", ["10/08/2022"], "Bullet", "blablabla"

    def input_tournament_data(self):
        dates_tournament = []
        tournament_name = pyip.inputStr("Nom du tournoi : ")
        place = pyip.inputStr("Lieu du tournoi : ")

        input_date = True
        while input_date == True:
            date_tournament = pyip.inputDate("Date (jjmmaaaa) : ", formats=['%d%m%Y'])
            dates_tournament.append(datetime.strftime(date_tournament, '%d/%m/%Y'))
            input_date = pyip.inputBool("Voulez-vous ajouter une date au tournoi Oui = t Non = f: ", "True", "False")

        time_control = pyip.inputMenu(["Bullet", "Blitz", "Coup rapide"], numbered=True)
        tournament_description = pyip.inputStr("Description du tournoi : ", blank=True)

        return tournament_name, place, dates_tournament, time_control, tournament_description

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

    def display_tournament_in_progress(self, remaining_rounds): # Vérifier si pas inutile
        print("\nCette action n'est pas possible tant que le tournoi n'est pas terminé !\n")
        print(f"Il reste {remaining_rounds} tournée(s) à jouer pour ce tournoi.")

    def display_tournament_total_scores(self, remaining_rounds):

        print(f"Il reste {remaining_rounds} tournée(s) à jouer pour ce tournoi.\nLes scores à ce stade du tournoi : "
              f"\n")
        tournament_final_scores_sorted = sorted(self.tournament.tournament_final_scores, key=lambda x: x[1],
                                                reverse=True)
        for element in sorted(self.tournament.tournament_final_scores, key=lambda x: x[1], reverse=True):
            print(f"{tournament_final_scores_sorted.index(element)+1}. {element[0].first_name} "
                  f"{element[0].last_name} (ID {element[0].player_id}) - Score : {element[1]} ;")

    def input_tournament_player_new_rank(self):

        new_rank = pyip.inputInt(prompt="\nSaisir le nouveau classement du joueur : \n")

        return new_rank

    def display_all_players_by_rank(self):
        pass