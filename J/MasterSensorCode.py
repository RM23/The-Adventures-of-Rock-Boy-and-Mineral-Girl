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
evalTime = 10

GPIO.setwarnings(False)

#Fucntion that checks for changes in acclerometer readings to simulate taking strike and dip
def accelCode():
    #number of bits in the I2C input
    bits = 16
    #list of previous readings for comparison
    prvList = []
    #get I2C bus - initial bus to channel 1
    bus = smbus.SMBus(1)
    
    for i in range(evalTime):
        #put register in active mode
        bus.write_byte_data(0x1D, 0x2A, 1)
        time.sleep(0.05)

        #read from status register
        data = bus.read_i2c_block_data(0x1D, 0x00, 7)

        #put register in standby mode
        bus.write_byte_data(0x1D, 0x2A, 0)
        time.sleep(0.05)

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
                return True
                break

        #store current data for comparison in next cycle of loop
        prvList = acclList
        print("Waiting")
    return False

#Function that checks for button inputs
def buttonCode():
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
    for i in range(evalTime):
        blueInput = GPIO.input(bluePin)
        greenInput = GPIO.input(greenPin)
        yellowInput = GPIO.input(yellowPin)
        redInput = GPIO.input(redPin)
        if blueInput == 1:
            return "Blue"
            break
        elif greenInput == 1:
            return "Green"
            break
        elif yellowInput == 1:
            return "Yellow"
            break
        elif redInput == 1:
            return "Red"
            break
        time.sleep(.1)
    return False

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
def flexCode():
    #start tracking flex sensor readings
    for i in range(evalTime):
        firstReading = readAdc(0)
        time.sleep(.1)
        secondReading = readAdc(0)
        #test if sensor is flexed
        if firstReading - secondReading > 20:
            return True
            break
    return False    

#Function that detecs pressure on force resist sensor
def forceCode():
    for i in range(evalTime):
        #Takes in reading on Force Resistor
        reading = readAdc(0)
        #Detects if applied forces exceed comparison value
        if reading > 500:
            return True
            break
        time.sleep(.1)
    
    return False

#Function that detects when the Trimpot Knob is turned
def knobCode():
    for i in range(evalTime):
        #First measurement of Trimpot position
        first = readAdc(0)
        #Delay between readings
        time.sleep(.1)
        #Second measurement of Trimpot position
        second = readAdc(0)
        #Comparison to check if knob has been rotated
        if first - second > 10:
            return True
            break
    
    return False
    
def magnetCode():
    #Sets pin to read Reed Switch input
    reedPin = 18
    #Set the correct board configuration
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(reedPin, GPIO.IN, GPIO.PUD_DOWN)

    for i in range(evalTime):
        #Takes in reading from Reed Swith
        reading = GPIO.input(reedPin)
        #Test if input is on
        if reading == 1:
            return True
            break
        time.sleep(.1)
    return False

#Bitstrings for photocell ADC chip readings
def bitstring(n):
    s = bin(n)[2:]
    return "0"*(8-len(s)) + s

#ADC chip reader code for photocell
def read(adc_channel):
    #Specify channel
    spi_channel = 0
    #Create Spidev object
    spi2 = spidev.SpiDev()
    #Open specific port and channel
    spi2.open(adc_channel, spi_channel)
    #set max speed
    spi2.max_speed_hz = 1000000
    #cmd corrections
    cmd = 128
    if adc_channel:
        cmd += 32
    #Read xfer2 method
    reply_bytes = spi2.xfer2([cmd, 0])
    #Join to bitstring
    reply_bitstring = ''.join(bitstring(n) for n in reply_bytes)
    #Slice reply
    reply = reply_bitstring[5:15]
    #return data formatted in base 10
    return int(reply,2) / 2**10

def photocellCode():
    for i in range(evalTime):
        firstRead = read(0)
        time.sleep(.1)
        secondRead = read(0)
        print(firstRead, secondRead)
        if firstRead == secondRead:
            return True
            break

    return False

def checkAll():
    flexPin = 4
    forcePin = 5
    knobPin = 6
    photoPin = 12
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(flexPin, GPIO.OUT)
    GPIO.setup(forcePin, GPIO.OUT)
    GPIO.setup(knobPin, GPIO.OUT)
    GPIO.setup(photoPin, GPIO.OUT)

    GPIO.output(flexPin, False)
    GPIO.output(forcePin, False)
    GPIO.output(knobPin, False)
    GPIO.output(photoPin, False)
    
    pinList = [flexPin, forcePin, knobPin, photoPin]
    while True:
        for pin in pinList:
            if pin == flexPin:
                GPIO.output(flexPin, True)
                if flexCode() == True:
                    return "Flex"
                    break
                else:
                    GPIO.output(flexPin, False)

            if pin == forcePin:
                GPIO.output(forcePin, True)
                if forceCode() == True:
                    return "Force"
                    break
                else:
                    GPIO.output(forcePin, False)

            if pin == knobPin:
                GPIO.output(knobPin, True)
                if knobCode() == True:
                    return "Knob"
                    break
                else:
                    GPIO.output(knobPin, False)

            if pin == photoPin:
                GPIO.output(photoPin, True)
                if photocellCode() == True:
                    return "Photocell"
                    break
                else:
                    GPIO.output(photoPin, False)

        if magnetCode() == True:
            return "Magnet"
            break

        color = buttonCode()
        if color != False:
            return color
            break

        if accelCode() == True:
            return "Accelerometer"
            break
print(accelCode())
#print(checkAll())
                
    

