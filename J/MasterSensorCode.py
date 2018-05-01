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
evalTime = 20
flexLimit = 442
forceLimit = 100
photoLimit = .4

GPIO.setwarnings(False)

#Fucntion that checks for changes in acclerometer readings to simulate taking strike and dip
def i2cRead():
    #number of bits in the I2C input
    bits = 16
    #get I2C bus - initial bus to channel 1
    bus = smbus.SMBus(1)
    
    #put register in active mode
    bus.write_byte_data(0x1D, 0x2A, 1)
    time.sleep(0.05)

    #read from status register
    data = bus.read_i2c_block_data(0x1D, 0x00, 7)

    #put register in standby mode
    bus.write_byte_data(0x1D, 0x2A, 0)
    time.sleep(0.05)

    #convert input into x,y,z components
    readings = []
    for i in range(3):
            accl = (data[i+1]*256 + data[i+2])/bits
            if accl > 2047:
                accl -= 4096
            readings.append(accl)
    #return readings for x,y,z
    return readings


def analogCode():
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
    #Sets pin to read Reed Switch input
    reedPin = 18
    #Setup Reed Switch pin
    GPIO.setup(reedPin, GPIO.IN, GPIO.PUD_DOWN)

    #test all of the analog inputs
    for i in range(evalTime):
        #Test accelerometer
        #create initial list of readings
        data1 = i2cRead()
        #delay between readings
        time.sleep(.1)
        #creates second list of readings
        data2 = i2cRead()
        #check for changes
        if abs(data1[0]-data2[0]) > 100 or abs(data1[2] - data2[2]) > 100:
            return "Acceleromter"
            break

        #Test Buttons
        #assigns inputs for each button
        blueInput = GPIO.input(bluePin)
        greenInput = GPIO.input(greenPin)
        yellowInput = GPIO.input(yellowPin)
        redInput = GPIO.input(redPin)
        if blueInput == 1:
            print("Turn Knob")
            action = knobCode()
            if action == True:
                return "Scratch"
                break
        elif greenInput == 1:
            return "Acid"
            break
        elif yellowInput == 1:
            print("Turn Knob")
            action = knobCode()
            if action == True:
                return "Streak"
                break
        elif redInput == 1:
            return "Run"
            break

        #Test Reed switch
        #takes in reading from Reed Swith
        reading = GPIO.input(reedPin)
        #Test if input is on
        if reading == 1:
            return "Magnet"
            break
        

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
    print("Flex")
    #start tracking flex sensor readings
    for i in range(evalTime):
    #while True:
        reading = readAdc(0)
        print(reading)
        
        #test if sensor is flexed
        if reading == flexLimit:
            return True
            break

#Function that detecs pressure on force resist sensor
def forceCode():
    print("Force")
    for i in range(evalTime):
    #while True:
        #Takes in reading on Force Resistor
        reading = readAdc(0)
        print(reading)
        #Detects if applied forces exceed comparison value
        if reading < forceLimit:
            return True
            break

#Function that detects when the Trimpot Knob is turned
def knobCode():
    knobPin = 6
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(knobPin, GPIO.OUT)
    GPIO.output(knobPin, True)
    while True:
        #First measurement of Trimpot position
        first = readAdc(0)
        #Delay between readings
        time.sleep(.1)
        #Second measurement of Trimpot position
        second = readAdc(0)
        #Comparison to check if knob has been rotated
        if abs(first - second) > 10:
            return "Speciman Scratched"
            break

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
    print("Photo")
    for i in range(evalTime):
    #while True:
        reading = read(0)
        print(reading)
        if reading < photoLimit:
            return True
            break
    

def checkAll():
    flexPin = 4
    forcePin = 5
    photoPin = 12
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(flexPin, GPIO.OUT)
    GPIO.setup(forcePin, GPIO.OUT)
    GPIO.setup(photoPin, GPIO.OUT)
    
    GPIO.output(flexPin, False)
    GPIO.output(forcePin, False)
    GPIO.output(photoPin, False)
    
    pinList = [flexPin, forcePin, photoPin]
    while True:
        for pin in pinList:
            
            if pin == flexPin:
                GPIO.output(pin, True)
                if flexCode() == True:
                    return "Flex"
                    break
                GPIO.output(pin, False)
                
            elif pin == forcePin:
                GPIO.output(pin, True)
                if forceCode() == True:
                    return "Force"
                    break
                GPIO.output(pin, False)
                
            elif pin == photoPin:
                GPIO.output(pin, True)
                if photocellCode() == True:
                    return "Photocell"
                    break
                GPIO.output(pin, False)
        otherSensors = analogCode() 
        if otherSensors != None :
            return otherSensors
            break

print(checkAll())


                
    

