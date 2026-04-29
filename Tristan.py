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
        if event == 1:
            print("you missed the secret event")
        elif event == 2:
            print("secret event is here")
secret_event()
def secret_event():
        if event == 2:
            print("you completed the secret event")
        elif event == 1:
            print("you felled the secret event")
secret_event()
