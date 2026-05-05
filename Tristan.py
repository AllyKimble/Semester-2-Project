import random

# random events and rare events
def zombie_event():
    global event
    event = random.randint(1, 2)
    print("An Event is on it's way")
    if event == 1:
        print("Event1:Zombie_rush has appeared")
    elif event == 2:
        print("Event2:Zombie_horde has appeared")
zombie_event()

def secret_event2():
    x = random.randint(1, 2)
    if x == 1:
        print("you completed the secret event")
    else:
        print("you felled the secret event")

def secret_event1():
    if event == 1:
        print("you missed the secret event")
    elif event == 2:
        print("secret event is here")
        secret_event2()
secret_event1()

class jwi:
    def __init__(self, hp, damage, weight):
        self.hp = hp
        self.damage = damage
        self.weight = weight
