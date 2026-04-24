import random
event = random.randint(1, 2)

# random events and rare events
def zombie_event():
        print("An Event is on it's way")
        if event == 1:
            print("Event1:Zombie_rush has appeared")
        elif event == 2:
            print("Event2:Zombie_Boss has appeared")
zombie_event()

def secret_event():
        print("secret event has appeared")
        if event == 1:
            print("you completed the secret event")
        elif event == 2:
            print("you filed the secret event")
secret_event()
#big boss on day what ever
class Zombie_Boss:
    def __init__(self, hp, speed, damage):
        self.hp = hp
        self.speed = speed
        self.damage = damage
boss = Zombie_Boss(150, 5, 15)
print('zombie_boss')
print(boss.hp)
print(boss.speed)
print(boss.damage)
#NEED TO MAKE BOSS SPAWN RANDOM