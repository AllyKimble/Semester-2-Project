import random


event = random.randint(1, 2)

def zombie_event():
        print("An EVENT is coming")
        if event == 1:
            print("Event 1 is coming")
        elif event == 2:
            print("Event 2 is coming")

zombie_event()