import RPi.GPIO as GPIO
import time

reedPin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(reedPin, GPIO.IN, GPIO.PUD_DOWN)

while True:
    reading = GPIO.input(reedPin)
    if reading == 1:
        print("It's Magnetic!!")
        break
    else:
        print("Waiting")
    time.sleep(.5)
