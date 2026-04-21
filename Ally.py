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
