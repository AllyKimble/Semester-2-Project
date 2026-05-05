import Ally, random

#Introduction
def introduction():
    print("Hello! this is a zombie apocalypes game where you can go through many different scenarios, bosses, loot, and even a dog!! ")
    print("Earth has been seized by zombies caused by an evil scientist called Dr. Treysaurus")
#follow the trail func
def day_5():
    print("You have decided to follow the trail of mysterious goo and you follow it for 1 hour through the woods")
    print("Following the trail, It has led you up to an abandoned cave")
    day_5av = input("What would you like your action to be ")
    print('1. Search the cave alone (very high risk)')
    print('2. Wait for the entity to come out and attack it (Moderate Risk, High Reward')
    if scout_thing == True and Scout.health >= 0:
        print('3. Have scout look first( Very High Risk, High reward')
    if day_5av == '1':
        a = random.randint(1,6)
        b = random.randint(1,3)
        if a == 1:
            print("You have gone into the cave and see a giant zombie monster boss sleeping")
            q = input("What would you like your next action to be ")
            print("1. Attack it while it's asleep (Low risk, High reward)")
            print('2. Wake it up and ask it to not destroy your base again (High risk high reward')
            print("3. Realize this isn't for you and go back to your destroyed base ( No risk, No reward")
            if q == 1:
                print("You attack it while it is asleep and deal 90 out of 100 of the enemy's health before it wakes up and attacks you")

            #Need a zombie boss class
        elif b == 2:
            print("")

#Start of day 5
print("You have returned back to camp and see that you camp has been ravenged by a mysterious entity. Leaving behind a trail of mysterious goo.")
day_5q = str(input("Would you like to follow the trail and get revenge (High Risk, High reward)or stay and rebuild your camp(Low chance and Low reward)(y/n):"))
if day_5q == "y" or "Y":
    day_5()
if day_5q == "n" or "N":
    print("You have chosen to do something else")
else:
    print("Pleaser choose and valid answer")
    print(day_5q)