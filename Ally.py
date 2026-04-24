#Zombie/ survival game?#



import random
import time

#class for player#

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.food = 1
        self.weapon = "Fists"
        self.inventory = ["Map", "Flashlight", "Socks", "Water Flask"]


name = input("Enter your survivor's name: ")
player = Player(name)

day = 1
choices_made = 0

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

print("Welcome " + player.name + "!")
print("Survive for 7 days in the zombie apocalypse!")

print("--- Day "  ,day,  " ---")
print("Health: ", player.health)
print("Food: ", player.food)
print("Weapon:", player.weapon)
print("Inventory:", player.inventory)


while player.health > 0 and day == 1:


    print("~~~ Choose your action ~~~")
    print("1. Search an abandoned house")
    print("2. Fight a zombie")
    print("3. Eat some lettuce")
    print("4. Rest")
    print("5. Eat the zombie")
    print("6. View inventory")

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

    if player.health > 100:
        player.health = 100
        print("Health: ", player.health)
        print("Food: ", player.food)

    if choices_made == 7:
        days()
        choices_made = 0

    if player.health <= 0:
        print("Oh no! You have died! GAME OVER")
        break


#Scavenging/Searching day#

if day == 2:

    print("--- Day "  ,day,  " ---")
    print("Health: ", player.health)
    print("Food: ", player.food)
    print("Weapon:", player.weapon)
    print("Inventory:", player.inventory)

while player.health > 0 and day == 2:
    print("~~~ Choose your action ~~~")
    print("1. Eat some scrumptious lettuce.")
    print("2. Rest.")
    print("3. Set up camp.")
    print("4. Look for people.")
    print("5. Use the last battery on your phone to play roblox.")
    print("6. Make a farm.")
    print("7. Go for a run.")

    choice = input("Enter your choice(1-7): ")

    if choice == "1":
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

    if choice == "2":
        choices_made += 1
        print("You rested and gained health")
        player.health += 5
        print("Health: ", player.health)

    if choice == "3":
        print("You decided to set up camp!")
        a = random.randint(1, 10)
        if a == 1:
            print("You managed to light a fire!")
            player.health += 5
            print("Health: ", player.health)
        elif a == 2:
            print("You tried to light a fire, but did not succeed. :(")
        elif a == 3:
            print("A spark landed on your shirt! You now have no shirt.")
            player.health -= 5
            print("Health: ", player.health)
        elif a == 4:
            print("You managed to set up a tent for the night.")
            player.health += 5
            print("Health: ", player.health)
        elif a == 5:
            print("You tried to set up a tent for the night, but did not succeed. :(.")
        elif a == 6:
            print("You decide to fry some lettuce over a fire!")
            player.food += 1
            print("Food: ", player.food)
        elif a == 7:
            print("You dropped your lettuce in the fire and tried to grab it! You burned your hand!")
            player.health -= 5
            player.food -= 1
            print("Health: ", player.health)
            print("Food: ", player.food)
        elif a == 8:
            damage = random.randint(5, 30)
            print("A zombie showed up while you were setting up! It attacks you!")
            player.health -= damage
            print("Health: ", player.health)
        elif a == 9:
            print("You hear a voice from the foliage. You walk over and find a small, purple cricket who is wearing a top hat, and a small pair of golden socks. It beckons you over, and hands you a small golden key. It looks you in the eyes, before jumping into the fire with a small scream. You pocket the key.")
            player.inventory.append(player.inventory.pop("Golden Key"))



