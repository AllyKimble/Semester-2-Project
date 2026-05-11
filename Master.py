#Scrum Doc: https://docs.google.com/document/d/1Rq5uj-W8qs1zOzi6sr5fjO4l766T5EL7Kjp9eIChGos/edit?tab=t.0

# Zombie Survival Game
# semester project

import random
import time

# random imports we probably dont need but it looks cool
from math import *
from time import sleep


# PLAYER

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.food = 3
        self.weapon = "Fists"
        self.inventory = ["Flashlight", "Socks", "Water Flask"]


# MONSTER

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 100


# SCOUT DOG CLASS
# class Scout:
#    def __init__(self, health, energy, damage):
#        self.health = health
#        self.energy = energy
#        self.damage = damage
# Scout = Scout(50, 100, 25)
# scout_thing = 1
# def scout_mechanic():
#   if scout_thing == True and Scout.health >= 0:
#       while Scout.health >= 0:
#           scout_question = str(input("Would you like to use scout?(y/n):"))
#           if scout_question == "y":
#               print("Would you like to use scout?")
#               print("What would you like scout to do?")
#               print("1. Look for food (Medium risk, medium prize")
#               print("2. look for an weapon crate (High risk, High prize)")
#               print("3. Feed her, she has:", Scout.health, "health, and", Scout.energy, "energy")
#               print("4. Pet her (Nevermind)")
#               Scout_choice = input("Enter your choice: ")
#               if Scout_choice == "1":
#                   scout1 = random.randint(1, 12)
#                   scout2 = random.randint(1, 6)
#                   if scout1 == 1:
#                       player.food += 5 and Scout.energy - 20
#                       print("Scout found you +5 food, But took -20 of her energy")
#                       print("Her new stats: Health:", Scout.health, "Energy:", Scout.energy)
#                   elif scout2 == 1:
#                       Scout.health -= 20 and Scout.energy - 20
#                       print("Scout got attacked by an zombie. - 20 scout health and -20 scout energy")
#                       print("Her new stats: Health:", Scout.health, "Energy:", Scout.energy)
#                   else:
#                       player.food += 1 and Scout.energy - 20
#                       print("Scout found you food. + 1 food and -20 Scout energy")
#               if Scout_choice == "2":
#                   scout1 = random.randint(1, 12)
#                   scout2 = random.randint(1, 4)
#                   if scout1 == 1:
#                        print("It has been 5 hours since scout has left. It is getting dark and you try to find her. YOu decide to leave and assume she is dead.")
#                        Scout.health = 0
#                    if scout2 == 1:
#                        print("Scout has came back and has led you to an weapons crate with an Assault Rifle and 3 medkits. ")
#                        player.inventory.append("Medkit"*3)
#                        player.weapon = "Assault Rifle"

class ScoutDog:
    def __init__(self):
        self.health = 50
        self.energy = 100
        self.damage = 25


Scout = ScoutDog()

# START GAME

name = input("Enter your survivor's name: ")
player = Player(name)

day = 1
choices_made = 0

print("\nWelcome", player.name + "!")
print("Try to survive 7 days in the zombie apocalypse...")
print("Good luck. You are probably doomed.\n")


# FUNCTIONS

def show_stats():
    print("\n========================")
    print("DAY:", day)
    print("Health:", player.health)
    print("Food:", player.food)
    print("Weapon:", player.weapon)
    print("Inventory:", player.inventory)
    print("========================\n")


def next_day():
    global day
    global choices_made

    day += 1
    choices_made = 0

    if day <= 6:
        print("\n===== IT IS NOW DAY", day, "=====\n")


def zombie_attack(min_damage, max_damage):
    damage = random.randint(min_damage, max_damage)

    # weapon buffs because realism
    if player.weapon == "Fork of Fear":
        damage -= 5

    elif player.weapon == "AR-15":
        damage -= 15

    elif player.weapon == "Knife":
        damage -= 8

    elif player.weapon == "Hatchet":
        damage -= 10

    elif player.weapon == "Battering Ram":
        damage -= 12

    elif player.weapon == "Rubber Chicken":
        damage -= 2
        print("The Rubber Chicken squeaks aggressively.")

    if damage < 0:
        damage = 0

    player.health -= damage

    print("A zombie attacks you!!")
    print("You lost", damage, "health!")


def eat_food():
    global choices_made

    if player.food > 0:

        player.food -= 1
        player.health += 10

        if player.health > 100:
            player.health = 100

        print("You ate some scrumptious lettuce.")
        print("Health:", player.health)

        choices_made += 1

    else:

        print("You have no food left T_T")


# =========================
# SCOUT MECHANIC
# =========================

def scout_mechanic():
    if "Scout" not in player.inventory:
        print("You dont have Scout.")
        return

    if Scout.health <= 0:
        print("Scout has sadly passed away...")
        return

    print("\n--- SCOUT MENU ---")
    print("1. Look for food")
    print("2. Look for weapons")
    print("3. Feed Scout")
    print("4. Pet Scout")
    print("5. Check Scout stats")

    scout_choice = input("Choose: ")

    if scout_choice == "1":

        Scout.energy -= 20

        result = random.randint(1, 5)

        if result == 1:
            player.food += 5
            print("Scout found LOTS of lettuce!!!")

        elif result == 2:
            player.food += 2
            print("Scout found a can of beans.")

        elif result == 3:
            Scout.health -= 15
            print("Scout got attacked by zombies!!")

        elif result == 4:
            print("Scout found nothing.")

        elif result == 5:
            print("Scout stole food from a zombie somehow.")
            player.food += 3

    elif scout_choice == "2":

        Scout.energy -= 30

        result = random.randint(1, 5)

        if result == 1:
            print("Scout found an AR-15!")

            player.weapon = "AR-15"

            if "AR-15" not in player.inventory:
                player.inventory.append("AR-15")

        elif result == 2:
            print("Scout found Medkits!")
            player.inventory.extend(["Medkit", "Medkit"])

        elif result == 3:
            Scout.health -= 20
            print("Scout got injured.")

        elif result == 4:
            print("Scout found a Rubber Chicken.")
            player.weapon = "Rubber Chicken"
            player.inventory.append("Rubber Chicken")

        else:
            print("Scout found absolutely nothing.")

    elif scout_choice == "3":

        if player.food > 0:

            player.food -= 1
            Scout.health += 10
            Scout.energy += 20

            if Scout.health > 50:
                Scout.health = 50

            if Scout.energy > 100:
                Scout.energy = 100

            print("You fed Scout some lettuce.")

        else:
            print("No food left!")

    elif scout_choice == "4":

        print("Scout seems happy.")

    elif scout_choice == "5":

        print("Scout Health:", Scout.health)
        print("Scout Energy:", Scout.energy)

    else:

        print("Invalid choice.")


# DAY 1


while player.health > 0 and day == 1:

    show_stats()

    print("1. Search an abandoned house")
    print("2. Fight a zombie")
    print("3. Eat some scrumptious lettuce")
    print("4. Rest")
    print("5. Eat the zombie")
    print("6. View inventory")

    choice = input("Choose: ")

    if choice == "1":

        choices_made += 1

        find = random.randint(1, 4)

        if find == 1:

            print("You found lettuce!")
            player.food += 2

        elif find == 2:

            print("You found the legendary FORK OF FEAR.")
            player.weapon = "Fork of Fear"

        elif find == 3:

            print("You found socks. More socks.")
            player.inventory.append("Mysterious Socks")

        else:

            zombie_attack(10, 25)

    elif choice == "2":

        choices_made += 1
        zombie_attack(5, 30)

    elif choice == "3":

        eat_food()

    elif choice == "4":

        choices_made += 1

        print("You rest.")
        player.health += 10

        if player.health > 100:
            player.health = 100

    elif choice == "5":

        print("You ate the zombie.")
        print("Why would you do that.")
        print("You die instantly.")

        player.health = 0

    elif choice == "6":

        print(player.inventory)

    else:

        print("Invalid choice.")

    if choices_made >= 5:
        next_day()

# DAY 2


while player.health > 0 and day == 2:

    show_stats()

    print("1. Search the surrounding forest")
    print("2. Set up camp")
    print("3. Look for some survivors")
    print("4. Start a farm")
    print("5. Play roblox with 1% battery")
    print("6. Rest")
    print("7. View inventory")

    choice = input("Choose: ")

    if choice == "1":

        choices_made += 1

        result = random.randint(1, 6)

        if result == 1:
            print("You found some food.")
            player.food += 3

        elif result == 2:
            zombie_attack(10, 25)

        elif result == 3:
            print("You found a map.")
            player.inventory.append("Map")

        elif result == 4:
            print("You find footprints leading toward town.")

        elif result == 5:
            print("You hear a scream in the distance.")
            print("You run away.")

        else:
            print("You find nothing.")

    elif choice == "2":

        choices_made += 1

        camp = random.randint(1, 6)

        if camp == 1:
            print("You built a nice fire.")

        elif camp == 2:
            print("You burned yourself.")
            player.health -= 5

        elif camp == 3:
            print(
                "You hear a voice from the foliage. You walk over and find a small, purple cricket who is wearing a top hat, and a small pair of golden socks. It beckons you over, and hands you a small golden key. It looks you in the eyes, before jumping into the fire with a small scream. You pocket the key.")
            player.inventory.append("Golden Key")

        elif camp == 4:
            zombie_attack(15, 35)

        elif camp == 5:
            print("You accidentally set your socks on fire.")

        elif camp == 6:
            print("You make grilled lettuce.")
            player.food += 2

    elif choice == "3":

        choices_made += 1

        result = random.randint(1, 5)

        if result == 1:
            print("You find an old campfire.")

        elif result == 2:
            zombie_attack(5, 20)

        elif result == 3:
            print("As you put a survivor out of its misery, it whispers to you...")
            print("'Find the Golden Socks...'")

        elif result == 4:
            print("Someone waves at you then falls into a pit.")

        elif result == 5:
            print("You find a backpack filled with food.")
            player.food += 10

    elif choice == "4":

        choices_made += 1

        plant = random.randint(1, 5)

        if plant == 1:
            print("You planted some lettuce.")
            player.food += 5

        elif plant == 2:
            print("You planted some butter. Yes. Butter.")
            player.food += 20

        elif plant == 3:
            print("You planted some carrots.")
            player.food += 5

        elif plant == 4:
            print("You planted some potatoes.")
            player.food += 5

        elif plant == 5:
            print("You forgot to water the plants.")
            player.food -= 5

    elif choice == "5":

        choices_made += 1

        print("You try to play Dress To Impress.")
        print("There is no internet.")
        print("Your phone dies and you throw it out of anger.")

    elif choice == "6":

        choices_made += 1

        player.health += 10

        if player.health > 100:
            player.health = 100

        print("You rested and feel refreshed.")

    elif choice == "7":

        print(player.inventory)

    else:

        print("Invalid choice.")

    if choices_made >= 5:
        next_day()

# DAY 3

while player.health > 0 and day == 3:

    show_stats()

    print("You found an abandoned military camp!")

    print("1. Search for supplies")
    print("2. Search for weapons")
    print("3. Find some working vehicles")
    print("4. Train in the Boot Camp")
    print("5. Look for people")
    print("6. View inventory")

    choice = input("Choose: ")

    if choice == "1":

        choices_made += 1

        result = random.randint(1, 4)

        if result == 1:
            print("You found a Medkit!")
            player.inventory.append("Medkit")

        elif result == 2:
            print(
                "A small toy tank wheels its way in front of you. A small blue cricket jumps out. It is wearing war paint and a camo helmet. It salutes you and tosses you a silver key, before reentering the tank. It explodes.")
            player.inventory.append("Silver Key")

        elif result == 3:
            zombie_attack(10, 20)

        else:
            print("You found nothing.")

    elif choice == "2":

        choices_made += 1

        result = random.randint(1, 6)

        if result == 1:
            player.weapon = "AR-15"
            player.inventory.append("AR-15")
            print("You found an AR-15!")

        elif result == 2:
            player.weapon = "Knife"
            player.inventory.append("Knife")
            print("You found a Knife!")

        elif result == 3:
            player.weapon = "Hatchet"
            player.inventory.append("Hatchet")

        elif result == 4:
            player.weapon = "Battering Ram"
            player.inventory.append("Battering Ram")

        elif result == 5:
            player.weapon = "Rubber Chicken"
            player.inventory.append("Rubber Chicken")
            print("squeak squeak")

        else:
            print("You found a spoon! Wow! It's pure silver!")

    elif choice == "3":

        choices_made += 1

        result = random.randint(1, 5)

        if result == 1:
            player.inventory.append("Truck")
            print("You found a Truck!")

        elif result == 2:
            player.inventory.append("Tank")
            print("You found a Tank!")

        elif result == 3:
            player.inventory.append("Bike")
            print("You found a Bike!")

        elif result == 4:
            player.inventory.append("Roller Skates")
            print("You found Roller Skates!")

        else:
            print("You can't find a working vehicle.")

    elif choice == "4":

        choices_made += 1

        print("You train, hoping to look like 'The Rock'.")
        player.health += 15

        if player.health > 100:
            player.health = 100

    elif choice == "5":

        choices_made += 1

        result = random.randint(1, 3)

        if result == 1:
            print("You find fresh footprints, but who left them?")

        elif result == 2:
            zombie_attack(5, 15)

        else:
            print("You find a survivor but they start talking in brainrot. You turn and walk away slowly.")

    elif choice == "6":

        print(player.inventory)

    else:

        print("Invalid choice.")

    if choices_made >= 5:
        next_day()

# DAY 4

while player.health > 0 and day == 4:

    show_stats()

    print("You enter an abandoned hospital.")

    print("1. Search for life")
    print("2. Search for supplies")
    print("3. Take some medicine")
    print("4. Investigate the locked doors")
    print("5. Use a Ouija board")
    print("6. Use Scout")
    print("7. View inventory")

    choice = input("Choose: ")

    if choice == "1":

        choices_made += 1

        if "Scout" not in player.inventory:

            print("You hear loud barking.")

            found = input("Investigate? (y/n): ")

            if found.lower() == "y":
                print("You found Scout!")
                player.inventory.append("Scout")

        else:

            print("You decide to not investigate.")

    elif choice == "2":

        choices_made += 1

        result = random.randint(1, 3)

        if result == 1:
            print("You found a Medkit.")
            player.inventory.append("Medkit")

        elif result == 2:
            print("You found some lettuce!!!!")

        else:
            print("You find nothing.")

    elif choice == "3":

        choices_made += 1

        med = random.randint(1, 4)

        if med == 1:
            player.health += 10
            print("The medicine kind of helped.")

        elif med == 2:
            player.health += 20
            print("The medicine REALLY helped.")

        elif med == 3:
            player.health -= 20
            print("The medicine was bad! T-T")

        else:
            print("Nothing happened.")

    elif choice == "4":

        choices_made += 1

        if "Silver Key" in player.inventory:

            open_door = input("Use Silver Key? (y/n): ")

            if open_door.lower() == "y":
                print("A zombie horde bursts out!")
                player.health = 0

        else:

            print("The doors are locked.")

    elif choice == "5":

        choices_made += 1

        ghost = random.randint(1, 3)

        if ghost == 1:
            print("A Friendly ghost gives you food.")
            player.food += 3

        elif ghost == 2:
            print("A Spooky Scary ghost attacks!")
            player.health -= 10

        else:
            print("Nothing happens.")

    elif choice == "6":

        scout_mechanic()

    elif choice == "7":

        print(player.inventory)

    else:

        print("Invalid choice.")

    if player.health > 100:
        player.health = 100

    if choices_made >= 5:
        next_day()

# DAY 5

while player.health > 0 and day == 5:

    show_stats()

    print("You return to find your camp is covered in mysterious goo.")

    print("1. Fix you camp")
    print("2. Follow the goo trail into the woods")
    print("3. Train")
    print("4. Rest")
    print("5. Use Scout")
    print("6. View inventory")

    choice = input("Choose: ")

    if choice == "1":

        choices_made += 1

        print("You slipped in goo, but manage to get back up. But not without some injuries.")
        player.health -= 10

    elif choice == "2":

        choices_made += 1

        print("You find a creepy cave.")

        enter = input("Enter cave? (y/n): ")

        if enter.lower() == "y":

            print("A giant monster appears!")

            monster_damage = random.randint(10, 40)

            if player.weapon == "AR-15":
                monster_damage -= 15

            elif player.weapon == "Hatchet":
                monster_damage -= 10

            if monster_damage < 0:
                monster_damage = 0

            player.health -= monster_damage

            print("You lost", monster_damage, "health.")

            if player.health > 0:

                print("You defeated the monster!")

                if "Golden Key" in player.inventory:
                    print("You unlock a glowing chest...")
                    print("Inside are THE GOLDEN SOCKS!")

                    player.inventory.append("Golden Socks")

    elif choice == "3":

        choices_made += 1

        gain = random.randint(5, 15)

        player.health += gain

        if player.health > 100:
            player.health = 100

        print("Training montage complete.")

    elif choice == "4":

        choices_made += 1

        player.health += 10

        if player.health > 100:
            player.health = 100

        print("You rested.")

    elif choice == "5":

        scout_mechanic()

    elif choice == "6":

        print(player.inventory)

    else:

        print("Invalid choice.")

    if choices_made >= 5:
        next_day()

# DAY 6

while player.health > 0 and day == 6:

    show_stats()

    print("FINAL DAY")

    print("1. Search the city")
    print("2. Prepare some defenses")
    print("3. Call for rescue")
    print("4. Rest")
    print("5. Use Scout")
    print("6. View inventory")

    choice = input("Choose: ")

    if choice == "1":

        choices_made += 1

        result = random.randint(1, 4)

        if result == 1:
            print("You found some food.")
            player.food += 2

        elif result == 2:
            zombie_attack(15, 35)

        elif result == 3:
            print("You found some medicine.")
            player.health += 15

        else:
            print("You found a single bean.")

    elif choice == "2":

        choices_made += 1

        print("You prepare defenses.")

        defense = random.randint(1, 2)

        if defense == 1:
            print("Defenses successful.")

        else:
            print("Zombies break through!")
            player.health -= 15

    elif choice == "3":

        choices_made += 1

        if "Truck" in player.inventory or "Tank" in player.inventory:

            print("Military rescue is coming!")
            day = 7

        else:

            print("Nobody answers.")

    elif choice == "4":

        choices_made += 1

        player.health += 10

        if player.health > 100:
            player.health = 100

        print("You rested.")

    elif choice == "5":

        scout_mechanic()

    elif choice == "6":

        print(player.inventory)

    else:

        print("Invalid choice.")

    if choices_made >= 5:
        day = 7

# FINAL ENDINGS

#    if day == 7:
#       secret_1 = random.randint(1,76)
#       secret_2 = random.randint(1,32)
#       secret_3 = random.randint(1,20)
#       secret_4 = random.randint(1,8)

#       if secret_1 == 1:
#           print("You have survived seven days this is a very very are ending")
#       elif secret_2 == 1:
#           print("You have survived seven days, this is a very rare ending")
#       elif secret_3 == 1:
#           print("You have survived seven days, the Decepticons have now sieved earth and now you serve them for the rest of your life (bad rare ending) ")
#       elif secret_4 == 1:
#          print("You have survived seven days, you realise that the whole game has been a nightmare. Now you live an ordinary life as an minimum wage plumber(Good uncommon ending)")
#      else:
#          print("You have survived seven days, and now have been saved by a military base (Good common ending)")

print("\n======================")
print("FINAL ENDING")
print("======================")

if player.health <= 0:

    print("GAME OVER")
    print("You died in the apocalypse.")

else:

    if "Golden Socks" in player.inventory:

        print("TRUE ENDING")
        print("You saved the world using the Golden Socks!")

    elif "Tank" in player.inventory:

        print("MILITARY ENDING")
        print("You survived with the military!")

    elif "Scout" in player.inventory:

        print("BEST FRIEND ENDING")
        print("You and Scout survive together!")

    elif "Roller Skates" in player.inventory:

        print("FUNNY ENDING")
        print("You roller skate into the sunset!")

    else:

        print("NORMAL ENDING")
        print("You survived somehow.")

print("\nGame Over.")
