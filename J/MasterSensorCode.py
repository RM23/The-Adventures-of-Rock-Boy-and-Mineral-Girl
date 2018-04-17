#Josh Stackhouse
#4/17/18
#Code for all of the sensors and mechanical inputs to be used in Rock Boy and Mineral Girl"

import time
import smbus
import RPi.GPIO as GPIO
import spidev
"""Import time for delays between sensor tests
Import smbus for I2C connection for accelerometer
Import RPi.GPIO to control pins on the Pi Wedge
Import spidev for reading inputs from analog sensors through ADC chip"""

#Fucntion that checks for changes in acclerometer readings to simulate taking strike and dip
def accelTest(strike,dip):
    #number of bits in the I2C input
    bits = 16
    #list of previous readings for comparison
    prvList = []
    #get I2C bus - initial bus to channel 1
    bus = smbus.SMBus(1)
    
    while True:
        #put register in active mode
        bus.write_byte_data(0x1D, 0x2A, 1)
        time.sleep(0.5)

        #read from status register
        data = bus.read_i2c_block_data(0x1D, 0x00, 7)

        #put register in standby mode
        bus.write_byte_data(0x1D, 0x2A, 0)
        time.sleep(0.5)

        #convert input data into individual values for x, y, and z
        acclList = []
        for i in range(3):
            accl = (data[i+1]*256 + data[i+2])/bits
            if accl > 2047:
                accl -= 4096
            acclList.append(accl)

        #compare previous data to current data to detect if accelerometer has moved
        if len(prvList) > 0:
            if abs(acclList[0]-prvList[0])>50 or abs(acclList[2] - prvList[2])>50:
                print("Stirke and Dip Measured!!")
                break
        print("Waiting")

        #store current data for comparison in next cycle of loop
        prvList = acclList

    #return output for next function
    return strike, dip

#Function that checks for button inputs
def buttonTest(buttonPin,color):
    #sets pins to BCM mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonPin, GPIO.IN, GPIO.PUD_DOWN)

    #check for button press
    while True:
        buttonInput = GPIO.input(buttonPin)
        if buttonInput == 1:
            print(str(color), "button pressed")
            break
        print("Waiting for player input")
        time.sleep(1)
    #return output for next function
    return(color)

    
