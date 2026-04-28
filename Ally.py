#Zombie/ survival game?#



import random
import time
from idlelib.config_key import translate_key


#class for player#

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.food = 1
        self.weapon = "Fists"
        self.inventory = ["Flashlight", "Socks", "Water Flask"]


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
            print("You found the Fork of Fear!")
            player.weapon = "Fork of Fear"
        else:
            print("A zombie was inside the house and you got attacked!!! :O")
            player.health -= 25
            print("Health: ", player.health)

    if choice == "2":
        choices_made += 1
        damage = random.randint(5, 30)

        if player.weapon == "Fork of Fear":
            damage -= 5

        print("You fought a zombie!!")
        print("You lost,", damage, "health! :(")
        player.health -= damage
        print("Health: ", player.health)

    elif choice == "3":
        if player.food > 0:
            print("You ate some scrumptious lettuce!")
            player.food -= 1
            player.health += 5
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
    print("8. View inventory.")

    choice = input("Enter your choice(1-8): ")

    if choice == "1":
        if player.food > 0:
            print("You ate some scrumptious lettuce!")
            player.food -= 1
            player.health += 5
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
        choices_made += 1
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
            player.inventory.append("Golden Key")
            print("You now have The Golden Key.")
        elif a == 10:
            print("You attracted a zombie horde!")
            player.health -= random.randint(20, 50)
            print("Health: ", player.health)

    if choice == "4":
        choices_made += 1
        b = random.randint(1, 7)
        if b == 1:
            print("You search the surrounding forest for humans. You find nothing.")
        if b == 2:
            print("You search the surrounding forest for humans. You find an old campfire, and some footprints leading towards the town.")
        if b == 3:
            print("You call out, but only the wind answers... It's quiet.... Too quiet..")
            c = random.randint(1,2)
            if c == 1:
                print("You continue on.")
            elif c == 2:
                print("A zombie appears from behind a tree! You get attacked.")
                player.health -= random.randint(5, 20)
                print("Health: ", player.health)
        if b == 4:
            print("You find a dropped backpack with a map marked “SAFE?”")
            player.inventory.append("Map")
        if b == 5:
            print("Someone signals you from a distance but runs off before you get close.")
            d = random.randint(1,2)
            if d == 1:
                print("You decide to go back to camp.")
            elif d == 2:
                print("You decide to take a closer look.")
                print("Oh no! You fall in into a pit trap! You're injured, but manage to climb out.")
                player.health -= 10
                print("Health: ", player.health)
        if b == 6:
            print("You don't find people, but find a snowflake. Winter is coming.")
        if b == 7:
            print("You find a survivor, but they’re bitten.")
            e = random.randint(1,3)
            if e == 1:
                print("You decide to leave them behind.")
                f = random.randint(1,2)
                if f == 1:
                    print("you hear their cries, but don't turn back.")
                elif f == 2:
                    print("They jump forward and attack you from behind!")
                    player.health -= random.randint(5, 20)
                    print("Health: ", player.health)
            if e == 2:
                print("You decide to try and help them.")
                print("They lose control and attack you!")
                player.health -= random.randint(5, 20)
                print("Health: ", player.health)
            if e == 3:
                print("You put them out of their misery, but before you do, they manage to whisper to you. 'Find the socks, and save the world'")

    if choice == "5":
        choices_made += 1
        print("You decide to play dress to impress, but there is no internet and your phone dies while it was loading.")

    if choice == "6":
        choices_made += 1
        g = random.randint(1,5)
        if g == 1:
            print("You decide to plant lettuce!")
            player.food += 5
            print("Food: ", player.food)
        if g == 2:
            print("You decide to plant potatoes!")
            player.food += 5
            print("Food: ", player.food)
        if g == 3:
            print("You decide to plant corn!")
            player.food += 5
            print("Food: ", player.food)
        if g == 4:
            print("You decide to plant butter!")
            player.food += 20
            print("Food: ", player.food)
        if g == 5:
            print("You decide to plant carrots!")
            player.food += 5
            print("Food: ", player.food)

    if choice == "7":
        choices_made += 1
        print("You decide to go for a run.")
        h = random.randint(1,2)
        if h == 1:
            print("You run into some zombies!")
            player.health -= random.randint(5, 20)
            print("Health: ", player.health)
        elif h == 2:
            print("You have a nice refreshing run.")
            player.health += 10
            print("Health: ", player.health)

    if choice == "8":
        choices_made += 1
        print("inventory:", player.inventory)

    elif choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8":
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

if day == 3:

    print("--- Day ", day, " ---")
    print("Health: ", player.health)
    print("Food: ", player.food)
    print("Weapon:", player.weapon)
    print("Inventory:", player.inventory)

while player.health > 0 and day == 3:
    print("You found an abandoned military camp!")
    print("~~~ Choose your action ~~~")
    print("1. Eat some scrumptious lettuce.")
    print("2. Rest in one of the tents.")
    print("3. Search for supplies.")
    print("4. Look for people.")
    print("5. Find a working vehicle.")
    print("6. Search for weapons.")
    print("7. Use the boot camp.")
    print("8. View inventory.")

    choice = input("Enter your choice(1-8): ")

    if choice == "1":
        if player.food > 0:
            print("You ate some scrumptious lettuce!")
            player.food -= 1
            player.health += 5
            print("Food: ", player.food)
            print("Health: ", player.health)
            choices_made += 1
        else:
            print("No food left! T-T")
            print("Food: ", player.food)

    if choice == "2":
        choices_made += 1
        print("You push a skeleton out of a bed and take a nap.")
        player.health += 5
        print("Health: ", player.health)

    if choice == "3":
        choices_made += 1
        i = random.randint(1,4)
        if i == 1:
            print("You search a small tent and find a medkit!")
            player.inventory.append("Medkit")
            print(player.inventory)
        elif i == 2:
            print("You search a broken vehicle and fin a box of ammo!")
        elif i == 3:
            print("A small toy tank wheels its way in front of you. A small blue cricket jumps out. It is wearing war paint and a camo helmet. It salutes you and tosses you a silver key, before reentering the tank. It explodes.")
            player.inventory.append("Silver")
            print("You now have a Silver key!")
        elif i == 4:
            print("You found nothing :(")

    if choice == "4":
        choices_made += 1
        j = random.randint(1,3)
        if j == 1:
            print("you find fresh blood!")
            k = random.randint(1,3)
            if k == 1:
                print("You follow the trail and find a zombie!")
                player.health -= random.randint(5, 20)
                print("Health: ", player.health)
            elif k == 2:
                print("You find a fresh body...........")
            elif k == 3:
                print("You find a injured survivor!")
                l = random.randint(1,2)
                if l == 1:
                    print("You decide to put them out of their misery, but before you do, they manage to whisper to you 'The Golden socks.......'.")
                elif l == 2:
                    print("You decide to help them, but as you offer them food, they lunge forward!")
                    player.health -= random.randint(5, 20)
                    print("Health: ", player.health)
        elif j == 2:
            print("You find a fresh campfire, but no one in sight.")
        elif j == 3:
            print("You find a set of fresh tire tracks leading towards the city.")

    if choice == "5":
        choices_made += 1
        m = random.randint(1, 6)
        if m == 1:
            print("None of the vehicles around you work.")
        if m == 2:
            print("You find a truck, but as you try to start it, you explode!")
            player.health = 0
            print("Health: ", player.health)


nothing
explosion
tank
truck
bike
roller skates