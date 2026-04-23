#Things to work on:
#Scenarios, make an introduction to game/explain, fix the choices, fix and bugs
import random, time
#class for player#
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.food = 1
        self.weapon = "Fists"
        self.inventory = ["Map", "Flashlight", "Socks", "Water Flask"]
#Day_def
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
            print("You have survived seven days this is a very very are ending")
        elif secret_2 == 1:
            print("You have survived seven days, this is a very rare ending")
        elif secret_3 == 1:
            print("You have survived seven days, the Decepticons have now sieved earth and now you serve them for the rest of your life (bad rare ending) ")
        elif secret_4 == 1:
            print("You have survived seven days, you realise that the whole game has been a nightmare. Now you live an ordinary life as an minimum wage plumber(Good uncommon ending)")
        else:
            print("You have survived seven days, and now have been saved by a military base (Good common ending)")
#Choices_def
choices_made = 0
def choices():
    global choices_made
    print("~~~ Choose your action ~~~")
    print("1. Search an abandoned house")
    print("2. Fight a zombie")
    print("3. Eat some lettuce")
    print("4. Rest")
    print("5. Eat the zombie")
    print("6. View inventory")
    choices_made += 1
#usersname
name = input("Enter your survivor's name: ")
player = Player(name)
day = 1
#Start_of_Game
print("Welcome " + player.name + "!")
print("Survive for 7 days in the zombie apocalypse!")
print("Health: ", player.health)
print("Food: ", player.food)
print("Weapon:", player.weapon)
choices()

#first_choice
while player.health > 0 and day <= 6:
    choice = input("Enter your choice(1-6): ")
    if choice == "1":
        choices_made += 1
        find = random.randint(1, 3)

        if find == 1:
            print("You found some lettuce!")
            player.food +=  1
            print("Food: ", player.food)
        elif find == 2:
            print("You found the Fork of Wonder!")
            player.weapon = "Fork of Wonder"
        else:
            print("A zombie was inside the house and you got attacked!!! :O")
            player.health -= 25
            print("Health: ", player.health)

    if choice == "2":
        choices_made += 1
        damage = random.randint(5, 30)

        if player.weapon == "Fork of Wonder":
            damage -= 5

        print("You fought a zombie!!")
        print("You lost,", damage, "health! :(")
        player.health -= damage
        print("Health: ", player.health)

    elif choice == "3":
        choices_made += 1
        if player.food > 0:
            print("You ate some scrumptious lettuce!")
            player.food -= 1
            player.health += 2
            print("Food: ", player.food)
            print("Health: ", player.health)
            choices_made += 1
        else:
            print("No food left! T-T")
            print("Food: ", player.food)

    elif choice == "4":
        choices_made += 1
        print("You rested and gained health")
        player.health += 5
        print("Health: ", player.health)

    elif choice == "5":
        choices_made += 1
        print("You ate the zombie!? Now why would you do that? You have died.")
        player.health = 0
        print("Health: ", player.health)


    elif choice == "6":
        choices_made += 1
        print("inventory:", player.inventory)

    elif choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
            print("Invalid choice! Please try again.")

