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
#day 6
import random

def instructions():
    global instructions
    instructions = random.randint(1, 2)
    print('morning')
    if instructions == 1:
        print('not day 6 yet')
    elif instructions == 2:
        print('its day 6')
    if instructions == 2:
        print('its . finally . day . six . you . can . work . on . getting . help . off . the . GOOD . eye-land .')
        print('its . where . BAD . BAD . BADDDDD . stuff . happen . and . it . could . be . a . HAPPY . PLAYS . where . you . can . make . zombie . friends .')
        print('LETS  GO  GET  REEDY  KNOW . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! . ! .')
instructions()