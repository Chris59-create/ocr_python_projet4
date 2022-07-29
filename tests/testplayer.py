import random
from tournoisechecs.models.player import Player

players_test = []

for i in range(10):
    first_name = "Name" + str(random.randint(0,100))
    last_name = "Lastname" + str(random.randint(0,100))
    date_birth = date_birth = str(random.randrange(0,30))\
                              + str(random.randrange(0,12))\
                              + str(random.randrange(1000,9999))
    gender = random.choice(["F", "H"])
    players_test.append(Player(first_name, last_name, date_birth, gender))
    print(players_test[i].first_name)

for i in range(10):
    print(i, players_test[i].first_name, players_test[i].last_name, players_test[i].date_birth, players_test[i].gender,
          players_test[i].rank)

players_test[5].change_rank(10)
print(players_test[5].rank)

players_test[8].change_rank(4)
print(players_test[8].rank)
