#Josh Stackhouse
#4/3/2018
#Button Code

import RPi.GPIO as GPIO
import time as t

buttonPin = 27
buttonPrompt = True
timeBetweenTest = 1.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, GPIO.PUD_DOWN)

while buttonPrompt == True:
    buttonInput = GPIO.input(buttonPin)
    if buttonInput == 1:
        print("Button Pressed!")
        buttonPrompt = False
    else:
        print("Waiting for player input")
        t.sleep(timeBetweenTest)
print("Pass output to next funciton")
