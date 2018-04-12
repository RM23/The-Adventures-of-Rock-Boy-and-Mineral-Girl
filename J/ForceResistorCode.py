import time
import spidev

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 10000000

def readAdc(channel):
        #Read the raw data for channel 0 using the xfer2 method, which
        #sends AND recieves depending on the clock rise/fall.
        r = spi.xfer([int("01100000",2),15])

        #Get data
        #get 10 bit bitsring from r[0]
        s = bin(r[0])[2:].zfill(10)
        #append 8 '0's to last 2 bits from r[0]
        data = int(s[8:] + "0"*8, 2) +r[1]
        return data
while True:
    """reading = readAdc(0)
    if reading > 600:
        print("Success")
        break
    else:
        print("Waiting")
    time.sleep(1)"""
    print(readAdc(0))
    time.sleep(1)
