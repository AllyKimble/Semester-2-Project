#Zombie/ survival game?#



import random
import time
from idlelib.config_key import translate_key
from winreg import EnumKey



#class for player#

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.food = 1
        self.weapon = "Fists"
        self.inventory = ["Flashlight", "Socks", "Water Flask"]

class Monster:
    def __init__(self, name):
        self.name = Monster
        self.health = 100

name = input("Enter your survivor's name: ")
player = Player(name)

day = 1
choices_made = 0


#Class for Scout#

class Scout:
    def __init__(self, health, energy, damage):
        self.health = health
        self.energy = energy
        self.damage = damage
Scout = Scout(50, 100, 25)
scout_thing = 1
def scout_mechanic():
    if scout_thing == True and Scout.health >= 0:
        while Scout.health >= 0:
            scout_question = str(input("Would you like to use scout?(y/n):"))
            if scout_question == "y":
                print("Would you like to use scout?")
                print("What would you like scout to do?")
                print("1. Look for food (Medium risk, medium prize")
                print("2. look for an weapon crate (High risk, High prize)")
                print("3. Feed her, she has:", Scout.health, "health, and", Scout.energy, "energy")
                print("4. Pet her (Nevermind)")
                Scout_choice = input("Enter your choice: ")
                if Scout_choice == "1":
                    scout1 = random.randint(1, 12)
                    scout2 = random.randint(1, 6)
                    if scout1 == 1:
                        player.food += 5 and Scout.energy - 20
                        print("Scout found you +5 food, But took -20 of her energy")
                        print("Her new stats: Health:", Scout.health, "Energy:", Scout.energy)
                    elif scout2 == 1:
                        Scout.health -= 20 and Scout.energy - 20
                        print("Scout got attacked by an zombie. - 20 scout health and -20 scout energy")
                        print("Her new stats: Health:", Scout.health, "Energy:", Scout.energy)
                    else:
                        player.food += 1 and Scout.energy - 20
                        print("Scout found you food. + 1 food and -20 Scout energy")
                if Scout_choice == "2":
                    scout1 = random.randint(1, 12)
                    scout2 = random.randint(1, 4)
                    if scout1 == 1:
                        print("It has been 5 hours since scout has left. It is getting dark and you try to find her. YOu decide to leave and assume she is dead.")
                        Scout.health = 0
                    if scout2 == 1:
                        print("Scout has came back and has led you to an weapons crate with an Assault Rifle and 3 medkits. ")
                        player.inventory.append("Medkit"*3)
                        player.weapon = "Assault Rifle"

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
        if player.weapon == "AR-15":
            damage -= 9

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
            if player.weapon == "Fork of Fear":
                damage -= 5
            if player.weapon == "AR-15":
                damage -= 9
            print("A zombie showed up while you were setting up! It attacks you!")
            player.health -= damage
            print("Health: ", player.health)
        elif a == 9:
            print("You hear a voice from the foliage. You walk over and find a small, purple cricket who is wearing a top hat, and a small pair of golden socks. It beckons you over, and hands you a small golden key. It looks you in the eyes, before jumping into the fire with a small scream. You pocket the key.")
            player.inventory.append("Golden Key")
            print("You now have The Golden Key.")
        elif a == 10:
            damage = random.randint(20, 50)
            if player.weapon == "Fork of Fear":
                damage -= 5
            if player.weapon == "AR-15":
                damage -= 9
            print("You attracted a zombie horde!")
            player.health -= damage
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
        m = random.randint(1, 6)
        if m == 1:
            print("None of the vehicles around you work.")
        elif m == 2:
            print("You find a truck, but as you try to start it, you explode!")
            player.health = 0
            print("Health: ", player.health)
            choices_made += 1
        elif m == 3:
            print("You find a working tank!")
            if "Tank" in player.inventory:
                print("You already have one tank... You don't need two!")
            elif "Truck" in player.inventory:
                print("You already found a truck... You don't need a tank too!")
            elif "Bike" in player.inventory:
                print("You already found a bike... You don't need a tank too!")
            elif "Roller Skates" in player.inventory:
                print("You already found a pair of Roller Skates... You don't need a tank too!")
            else:
                player.inventory.append("Tank")
                choices_made += 1
        elif m == 4:
            print("You  find a working truck!")
            if "Truck" in player.inventory:
                print("You already have one truck... You don't need two!")
            elif "Tank" in player.inventory:
                print("You already found a tank... You don't need a truck too!")
            elif "Bike" in player.inventory:
                print("You already found a bike... You don't need a truck too!")
            elif "Roller Skates" in player.inventory:
                print("You already found a pair of Roller Skates... You don't need a truck too!")
            else:
                player.inventory.append("Truck")
                choices_made += 1
        elif m == 5:
            print("You  find a bike!")
            if "Bike" in player.inventory:
                print("You already have one bike... You don't need two!")
            elif "Tank" in player.inventory:
                print("You already found a tank... You don't need a bike too!")
            elif "Truck" in player.inventory:
                print("You already found a truck... You don't need a bike too!")
            elif "Roller Skates" in player.inventory:
                print("You already found a pair of Roller Skates... You don't need a bike too!")
            else:
                player.inventory.append("Bike")
                choices_made += 1
        elif m == 6:
            print("You found a pair of Roller Skates!")
            if "Roller Skates" in player.inventory:
                print("You already found a pair of Roller Skates... You don't need two!")
            elif "Bike" in player.inventory:
                print("You already found a Bike... You don't need Roller Skates too!")
            elif "Tank" in player.inventory:
                print("You already found a Tank... You don't need Roller Skates too!")
            elif "Truck" in player.inventory:
                print("You already found a Truck... You don't need Roller Skates too!")
            else:
                player.inventory.append("Roller Skates")
                choices_made += 1

    if choice == "6":
        choices_made += 1
        print("You go in search of weapons.")
        n = random.randint(1,7)
        if n == 1:
            print("You pry open an old crate, and find a Nuke! You quickly try to scramble away, but sadly, you set it off. The world around you explodes.")
            player.health = 0
            print("Health: ", player.health)
        elif n == 2:
            print("You find an AR-15!")
            player.inventory.append("AR-15")
            player.weapon = "AR-15"
        elif n == 3:
            print("You find a Rubber Chicken!?")
            player.inventory.append("Rubber Chicken")
            player.weapon = "Rubber Chicken"
        elif n == 4:
            print("You find a knife!")
            player.inventory.append("Knife")
            player.weapon = "Knife"
        elif n == 5:
            print("You find a hatchet!")
            player.inventory.append("Hatchet")
            player.weapon = "Hatchet"
        elif n == 6:
            print("you find a Riot Shield!")
            player.inventory.append("Riot Shield")
            player.weapon = "Riot Shield"
        elif n == 7:
            print("you find a Battering Ram!")
            player.inventory.append("Battering Ram")
            player.weapon = "Battering Ram"

    if choice == "7":
        choices_made += 1
        print("You decide to use the Boot Camp. You gain some health!")
        heal = random.randint(10, 30)
        player.health += heal
        if player.health >= 100:
            player.health = 100
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

if day == 4:

    print("--- Day ", day, " ---")
    print("Health: ", player.health)
    print("Food: ", player.food)
    print("Weapon:", player.weapon)
    print("Inventory:", player.inventory)

while player.health > 0 and day == 4:
    print("You find an abandoned Hospital!")
    print("~~~ Choose your action ~~~")
    print("1. Eat some scrumptious lettuce.")
    print("2. Rest in a medical bed.")
    print("3. Search for life.")
    print("4. Look for supplies.")
    print("5. Take some medicine.")
    print("6. Tend to your wounds.")
    print("7. Investigate a loud banging deep in the Hospital.")
    print("8. Use a Ouija board")
    print("9. View inventory.")
    if "Scout" in player.inventory:
        print("10. Use Scout.")


    if "Scout" in player.inventory:
        choice = input("Enter your choice(1-10): ")
    else:
        choice = input("Enter your choice(1-9): ")


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
        print("You decided to take a nap in a medical bed.")
        player.health += 5
        print("Health: ", player.health)

    if choice == "3":
        if "Scout" in player.inventory:
            print("There is no more life in the hospital. Go do something else.")
        else:
            choices_made += 1
            print("You decide to search the hospital for life.")
        p = input("While you are searching through the hospital, you hear a sound. Do you investigate? (Yes/No):")
        if p == "Yes" or p == "yes" or p == "YES" or p == "Y" or p == "y" or p == "Yep" or p == "Yeah" or p == "yeah"  or p == "yep":
            print("You decide to investigate the sound. You walk into a small room and see a dog hiding behind a box. You check her collar, her name is Scout!")
            player.inventory.append("Scout")
        if p == "No" or p == "no" or p == "NO" or p == "N" or p == "n" or p == "Nope" or p == "nope" or p == "nah" or p == "Nah":
            print("You decide to not investigate the sound and return to the main hall again.")

        if "Scout" in player.inventory:
            scout_mechanic()

    if choice == "4":
        choices_made += 1
        print("You decide to look for supplies.")
        q = random.randint(1, 2)
        if q == 1:
            print("You found a Medkit!")
            player.inventory.append("Medkit")
        elif q == 2:
            print("You did not find anything.")

    if choice == "5":
        choices_made += 1
        r = input("You find a cabinet of medicine, do you take some?(Yes/No):")
        if r == "Yes" or r == "yes" or r == "YES" or r == "Y" or r == "yes" or r == "y" or r == "Yep" or r == "Yeah" or r == "Yea" or r == "yea" or r == "yeah" or r == "yep":
            print("You decide to take some medicine!")
            s = random.randint(1, 4)
            if s == 1:
                print("You Gain 5 health.")
                player.health += 5
            elif s == 2:
                print("You Gain 10 health.")
                player.health += 10
            elif s == 3:
                print("You Gain 15 health.")
                player.health += 15
            elif s == 4:
                print("Oh no! The medicine you took was bad! You lose a LOT of health. :(")
                player.health -= 67
        elif r == "No" or r == "no" or r == "NO" or r == "N" or r == "n" or r == "Nope" or r == "nope" or r == "nah" or r == "Nah":
            print("You decide not to take some medicine.")

    if choice == "6":
        choices_made += 1
        print("You decide to tend to your wounds.")
        player.health += 10

    if choice == "7":
        choices_made += 1
        print("You decide to investigate the sound. You wall down a long hall, stopping before a set of metal doors. You can hear loud noises and banging from the other side. You try the door handle but the doors are locked.")
        if "Silver" in player.inventory:
            t = input("You feel the weight of the Silver key in your pocket. You pull it out and see that it would work in this door. Do you open it?(Yes/No):")
            if t == "Yes" or t == "yes" or t == "YES" or t == "Y" or t == "yes" or t == "y" or t == "Yep" or t == "Yeah" or t == "Yea" or t == "yea" or t == "yeah" or t == "yep":
                print("You decide to unlock the doors. You turn the key in the lock and pull the doors open. A horde of zombies pushes their way out and smothers you.")
                player.health = 0
            elif t == "No" or t == "no" or t == "NO" or t == "N" or t == "n" or t == "Nope" or t == "nope" or t == "nah" or t == "Nah":
                print("You decide to not open the doors, you pocket the key and turn away.")

    if choice == "8":
        choices_made += 1
        print("You find an old wooden Ouija Board. You sit down to use it.")
        u = random.randint(1, 3)
        if u == 1:
            print("A ghost appears! It seems friendy. It gives you 3 lettuce.")
            player.food += 3
        elif u == 2:
            print("A scary ghost appears!")
            player.health -= 5
        elif u == 3:
            print("Nothing happens...")

    if choice == "9":
        choices_made += 1
        print("Inventory:", player.inventory)

    elif choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
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

if day == 5:
    print("--- Day ", day, " ---")
    print("Health: ", player.health)
    print("Food: ", player.food)
    print("Weapon:", player.weapon)
    print("Inventory:", player.inventory)

while player.health > 0 and day == 5:
    print("You have returned back to camp and see that you camp has been ravaged by a mysterious entity. Leaving behind a trail of mysterious goo.")
    print("~~~ Choose your action ~~~")
    print("1. Eat some scrumptious lettuce.")
    print("2. Rest.")
    print("3. Fix your camp.")
    print("4. Follow the mysterious goo.")
    print("5. Train with" , player.weapon , ".")
    print("6. View inventory.")
    if "Scout" in player.inventory:
        print("7. Use Scout.")

    if "Scout" in player.inventory:
        choice = input("Enter your choice(1-7): ")
    else:
        choice = input("Enter your choice(1-6): ")

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

    elif choice == "2":
        choices_made += 1
        print("You rested and gained health")
        player.health += 5
        print("Health: ", player.health)

    elif choice == "3":
        choices_made += 1
        print("You decide to fix up camp!")
        print("While fixing up camp, you fall into a puddle of goo! You manage to crawl out of it, but not without damage.")
        player.health -= 15

    elif choice == "4":
        print("You decide to follow the mysterious trail of goo.")
        v = input("You come to an abandoned cave, would you like to explore it?(Yes/No):")
        if v == "Yes" or v == "yes" or v == "YES" or v == "Y" or v == "yes" or v == "y" or v == "Yep" or v == "Yeah" or v == "Yea" or v == "yea" or v == "yeah" or v == "yep":
            print("You decide to explore the cave.")
            if "Scout" in player.inventory:
                w = input("Would you like to send Scout in first?(Yes/No):")
                if w == "Yes" or w == "yes" or w == "YES" or w == "Y" or w == "yes" or w == "y" or w == "Yep" or w == "Yeah" or w == "Yea" or w == "yea" or w == "yeah" or w == "yep":
                    x = random.randint(1, 3)
                    if x == 1:
                        print("Scout returns after a few minutes with nothing.")
                    if x == 2:
                        print("Scout runs back out, terrified.")
                        y = input("Do you want to enter the cave?(Yes/No):")
                        if y == "Yes" or y == "yes" or y == "YES" or y == "Y" or y == "yes" or y == "y" or y == "Yep" or y == "Yeah" or y == "Yea" or y == "yea" or y == "yeah" or y == "yep":
                            print("You decide to enter the dark cave. Scout cowers behind you as you delve deeper. After 30 minutes of walking, the cave tunnel opens up to a large cavern. In the middle of it sits a giant monster. It looks up at you, and leaps forward, ready to attack.")
                            monster_damage =  random.randint(5, 50)

                    if x == 3:
                        print("Scout returns, and pulls you into the cave, excited.")

