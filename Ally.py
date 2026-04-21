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
        self.inventory = ["Map", "Flashlight", "Socks", "Water Flask"]  #List#

#User Input#
name = input("Enter your survivor's name: ")
player = Player(name)

day = 1

print("Welcome " + player.name + "!")
print("Survive for 7 days in the zombie apocalypse!")

#loop#

while player.health > 0 and day <= 7:

    print("--- Day "  ,day,  " ---")
    print("Health: ", player.health)
    print("Food: ", player.food)
    print("Weapon:", player.weapon)
    print("Inventory:", player.inventory)

    print("~~~ Choose your action ~~~")
    print("1. Search an abandoned house")
    print("2. Fight a zombie")
    print("3. Eat some lettuce")
    print("4. Rest")
    print("5. Eat the zombie")
    print("6. View inventory")

    choice = input("Enter your choice(1-5): ")

    if choice == "1":
        find = random.randint(1, 3)

        if find == 1:
            print("You found some lettuce!")
            player.food +=  1
        elif find == 2:
            print("You found the Fork of Wonder!")
            player.weapon = "Fork of Wonder"
        else:
            print("A zombie was inside the house and you got attacked!!! :O")
            player.health -= 25

    if choice == "2":
        damage = random.randint(5, 30)

        if player.weapon == "Fork of Wonder":
            damage -= 5

        print("You fought a zombie!!")
        print("You lost,", damage, "health! :(")
        player.health -= damage

    elif choice == "3":
        if player.food >0:
            print("You ate some scrumptious lettuce!")
            player.food -= 1
            player.health += 2
        else:
            print("No food left! T-T")

    elif choice == "4":
        print("You rested and gained health")
        player.health += 5
