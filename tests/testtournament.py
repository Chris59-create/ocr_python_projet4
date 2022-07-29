from tournoisechecs.models.tournament import Tournament
from tournoisechecs.models.player import Player
from tournoisechecs.models.round import Round

tournoi1 = Tournament("tournoi estival", "Solbach", 11121900, 12121900, "bullet")

test_instance = [Player("lastname1", "firstname1", 11111900, "H", 10), Player("lastname2", "firstname2", 11111900,
                                                                              "F", 9),
                 Player("lastname3", "firstname3", 11111900, "H", 2), Player("lastname4", "firstname4", 11111900,
                                                                             "F",3),
                 Player("lastname5", "firstname5", 11111900, "H", 6), Player("lastname6", "firstname6", 11111900,
                                                                             "F",4),
                 Player("lastname7", "firstname7", 11111900, "H", 3), Player("lastname8", "firstname8", 11111900,
                                                                             "F",0)]

for element in test_instance:
    tournoi1.add_player(element)

"""round = Round("test round")
tournoi1.add_round(round)

round = Round("test2 round")
tournoi1.add_round(round)
round.end_round()"""
   
print("Lieu : ", tournoi1.place)
"""print("Liste objets joueurs: ", tournoi1.tournament_players)
print("Nom de famille joueur2 : ", tournoi1.tournament_players[1].first_name)
print("Liste objets tours : ", tournoi1.rounds)
print("Nom tour1 : ", tournoi1.rounds[0].round_name)
print("Début du tour : ", tournoi1.rounds[0].start_date_time)
print("Tour : ", tournoi1.rounds[1].round_name)
print("Début : ", tournoi1.rounds[0].start_date_time)
print("Fin : ", tournoi1.rounds[1].end_date_time)"""