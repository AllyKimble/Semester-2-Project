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