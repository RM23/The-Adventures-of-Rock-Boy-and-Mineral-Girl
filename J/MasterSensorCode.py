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
        time.sleep(0.25)

        #read from status register
        data = bus.read_i2c_block_data(0x1D, 0x00, 7)

        #put register in standby mode
        bus.write_byte_data(0x1D, 0x2A, 0)
        time.sleep(0.25)

        #convert input data into individual values for x, y, and z
        acclList = []
        for i in range(3):
            accl = (data[i+1]*256 + data[i+2])/bits
            if accl > 2047:
                accl -= 4096
            acclList.append(accl)

        #compare previous data to current data to detect if accelerometer has moved
        if len(prvList) > 0:
            if abs(acclList[0]-prvList[0]) > 100 or abs(acclList[2] - prvList[2]) > 100:
                print("Stirke and Dip Measured!!")
                print(strike, dip)
                break
        else:
            print("Waiting")

        #store current data for comparison in next cycle of loop
        prvList = acclList

    #return output for next function
    return

#Function that checks for button inputs
def buttonTest():
    #set the pins for the different colored buttons
    bluePin = 27
    greenPin = 26
    yellowPin = 25
    redPin = 24
    #sets pins to BCM mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(bluePin, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.setup(greenPin, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.setup(yellowPin, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.setup(redPin, GPIO.IN, GPIO.PUD_DOWN)

    #check for button presses
    while True:
        blueInput = GPIO.input(bluePin)
        greenInput = GPIO.input(greenPin)
        yellowInput = GPIO.input(yellowPin)
        redInput = GPIO.input(redPin)
        if blueInput == 1:
            print("Blue button pressed")
            return
            break
        elif greenInput == 1:
            print("Green button pressed")
            return
            break
        elif yellowInput == 1:
            print("Yellow button pressed")
            return
            break
        elif redInput == 1:
            print("Red Button pressed")
            return
            break
        else:
            print("Waiting for player input")
        time.sleep(.5)

#Read ADC chip function
def readAdc(channel):

    #create spidev object
    spi = spidev.SpiDev()
    #opens specific port and channel
    spi.open(0,0)
    #max speed to prevent overworking pi
    spi.max_speed_hz = 10000000
    
    #Read the raw data using the xfer2 method
    r = spi.xfer([int("01100000",2),15])
    #get 10 bit bitstrin from r[0]
    s = bin(r[0])[2:].zfill(10)
    #append 8 0's to the last 2 bits from r[0]
    data = int(s[8:] + "0"*8, 2) + r[1]
    return data

#Function that detects if the flex sensor is bent
def flexTest():
    #Initial preivous reading variable
    prvReading = 0
    #Count for tracking amount of times flex sensor reading changes
    readingCount = 0
    #start tracking flex sensor readings
    while True:
        reading = readAdc(0)
        print(reading)
        if prvReading != 0:
            #record amount of times readings change
            if reading != prvReading:
                readingCount += 1
            else:
                print("Waiting")
        if readingCount == 3:
            print("Tenacity Tested")
            return
            break
        time.sleep(.5)
        #store reading to compare with next reading
        prvReading = reading

#Function that detecs pressure on force resist sensor
def forceTest():
    while True:
        reading = readAdc(0)
        if reading > 600:
            print("Fracture tested")
            return
            break
        else:
            print("Waiting")
        time.sleep(.5)


