import random
event = random.randint(1, 2)

# random events and rare events
def zombie_event():
        print("An Event is on it's way")
        if event == 1:
            print("Event1:Zombie_rush has appeared")
        elif event == 2:
            print("Event2:Zombie_horde has appeared")
zombie_event()

def secret_event():
        print("secret event has appeared")
        if event == 1:
            print("you completed the secret event")
        elif event == 2:
            print("you filed the secret event")
secret_event()
