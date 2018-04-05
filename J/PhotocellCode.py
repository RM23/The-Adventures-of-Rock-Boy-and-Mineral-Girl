from __future__ import division
import spidev
import time as t



lightAvg = []
lightCount = 0
lightPrompt = True
prvAvg = 1

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
    print(read(0))
    if len(lightAvg) == 10:
        del lightAvg[0]
    lightAvg.append(read(0))
    total = 0
    for i in lightAvg:
        total += i
    avg = total/len(lightAvg)
    #print(prvAvg)
    if avg > prvAvg:
        #print("Collecting Data")
        lightCount += 1
    else:
        #print("Waiting")
        pass
    
    #if lightCount > 5:
        #print("Success")
        #break
    prvAvg = avg
    t.sleep(.1)
    
