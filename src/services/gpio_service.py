import time

#import RPi.GPIO as GPIO


def updateState(requestedState):

    switch = 11
    if(currentState() != requestedState):
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(switch, GPIO.OUT)
        # GPIO.output(switch, GPIO.LOW)
        # time.sleep(0.25)
        # GPIO.output(switch, GPIO.HIGH)
        return 'this is dumb'

def currentState():

    switch = 13
    # GPIO.setup(switch, GPIO.IN)
    # return 1 == GPIO.input(switch)