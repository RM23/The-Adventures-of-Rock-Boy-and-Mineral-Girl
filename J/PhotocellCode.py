from __future__ import division
import spidev
import time as t


lightPrompt = True
readings = []

def bitstring(n):
    s = bin(n)[2:]
    return "0"*(8-len(s)) + s

def read(adc_channel):
    spi_channel = 0
    spi = spidev.SpiDev()
    spi.open(adc_channel, spi_channel)
    spi.max_speed_hz = 1000000
    cmd = 128
    if adc_channel:
        cmd += 32
    reply_bytes = spi.xfer2([cmd, 0])
    reply_bitstring = ''.join(bitstring(n) for n in reply_bytes)
    reply = reply_bitstring[5:15]
    return int(reply,2) / 2**10

while True:
    if len(readings) > 2:
        del readings[0]
    readings.append(read(0))
    if readings.count(readings[0]) == 2:
        print("Collected Data")
        break
    else:
        print("Waiting")
        pass
    
    t.sleep(.5)
    
