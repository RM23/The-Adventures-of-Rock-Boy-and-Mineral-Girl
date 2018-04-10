import numpy as np
import time as t
import spidev

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 10000000

def readAdc(channel):
    r = spi.xfer2([int("01100000",2), 15])

    s = bin(r[0])[2:].zfill(10)
    data = int(s[8:] + "0"*8, 2) + r[1]
    return data
while True:
    first = readAdc(0)
    t.sleep(.5)
    second = readAdc(0)
    if first != second:
        print("Scratch successful")
        break
    else:
        print("Waiting")
