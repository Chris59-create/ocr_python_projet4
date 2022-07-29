from tournoisechecs.models.round import Round
from tournoisechecs.models.match import Match


round1 = Round("roundtest")
print(round1.start_date_time)

round1.end_round()
print(round1.end_date_time)

match1 = Match((["player2", 0], ["player2", 1]))
round1.add_match(match1)
match2 = Match((["player3", 0], ["player4", 0]))
round1.add_match(match2)

print(round1.matches)

print(round1.matches[1][0][1])
