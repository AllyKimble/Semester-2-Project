#from Ally import Player
import random
day = 1
def days():
    global day
    day = day + 1
    if day <= 6:
        print("It is now day ", day)
    if day == 7:
        secret_1 = random.randint(1,76)
        secret_2 = random.randint(1,32)
        secret_3 = random.randint(1,20)
        secret_4 = random.randint(1,8)
        if secret_1 == 1:
            print("You have survived seven daysm this is a very very are ending")
        elif secret_2 == 1:
            print("You have survived seven days, this is a very rare ending")
        elif secret_3 == 1:
            print("You have survived seven days, the Decepticons have now sieved earth and now you serve them for the rest of your life (bad rare ending) ")
        elif secret_4 == 1:
            print("You have survived seven days, you realise that the whole game has been a nightmare. Now you live an ordinary life as an minimum wage plumber(Good uncommon ending)")
        else:
            print("You have survived seven days, and now have been saved by a military base (Good common ending)")

days()
days()
days()
days()
days()
days()
days()

#put days() to add a day

