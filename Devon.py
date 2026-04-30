#Things to work on: Random scenarios, attack and health, ask questions
#, try to fix scout possibly, try to work on another day, and make the weapons class work.
import random
#class for player#
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.food = 1
        self.weapon = ["Fists"]
        self.inventory = ["Map", "Flashlight", "Socks", "Water Flask"]
        self.medkits = 0

#Added Scout mechanic
class Scout_Character:
    def __init__(self, health, energy, damage):
        self.health = health
        self.energy = energy
        self.damage = damage
scout = Scout_Character(50, 100, 25)
scout_thing = 1
def scout_mechanic():
    if scout_thing == True and scout.health >= 0:
        while scout.health >= 0:
            scout_question = str(input("Would you like to use scout?(y/n):"))
            if scout_question == "y":
                print("Would you like to use scout?")
                print("What would you like scout to do?")
                print("1. Look for food (Medium risk, medium prize")
                print("2. look for an weapon crate (High risk, High prize)")
                print("3. Feed her, she has:", scout.health, "health, and", scout.energy, "energy")
                print("4. Pet her (Nevermind)")
                Scout_choice = input("Enter your choice: ")
                if Scout_choice == "1":
                    scout1 = random.randint(1, 12)
                    scout2 = random.randint(1, 6)
                    if scout1 == 1:
                        player.food += 5 and scout.energy - 20
                        print("Scout found you +5 food, But took -20 of her energy")
                        print("Her new stats: Health:", scout.health, "Energy:", scout.energy)
                    elif scout2 == 1:
                        scout.health -= 20 and scout.energy - 20
                        print("Scout got attacked by an zombie. - 20 scout health and -20 scout energy")
                        print("Her new stats: Health:", scout.health, "Energy:", scout.energy)
                    else:
                        player.food += 1 and scout.energy - 20
                        print("Scout found you food. + 1 food and -20 Scout energy")
                if Scout_choice == "2":
                    scout1 = random.randint(1, 12)
                    scout2 = random.randint(1, 4)
                    if scout1 == 1:
                        print("It has been 5 hours since scout has left. It is getting dark and you try to find her. YOu decide to leave and assume she is dead.")
                        scout.health = 0
                    if scout2 == 1:
                        print("Scout has came back and has led you to an weapons crate with an Assault Rifle and 3 medkits. ")
                        player.medkits += 3
                        player.weapon.append("Assault Rifle")
# Introduction
def introduction():
    print("Hello! this is a zombie apocalypes game where you can go through many different scenarios, bosses, loot, and even a dog!! ")
    print("Earth has been seized by zombies caused by an evil scientist called Dr. Treysaurus")
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
# Added a abandoned hospital scenario
def abandoned_hospital():
    thing1 = random.randint(1,12)
    thing2 = random.randint(1,7)
    thing3 = random.randint(1,3)
    if thing1 == 1:
        print("You found a gun (epic), and a first aid kit(Legendary)!!")
        player.weapon.append("Gun")
        player.medkits += 1
    if thing2 == 1 or thing2 == 2 or thing2 == 3 or thing2 == 4:
        print("You found a Dog, named scout. You become best friends!!")
        scout_thing = True
    if thing3 == 1:
        zombie_bite = random.randint(10,25)
        print("You got attacked by a zombie nurse, Minus", zombie_bite, "Hp")
        player.health -= zombie_bite
        print("Health: ", player.health)
    else:
        print("You found a baseball bat (common)")
