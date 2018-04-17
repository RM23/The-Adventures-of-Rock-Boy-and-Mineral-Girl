import time
import smbus

bits = 16
prvList = []
bus = smbus.SMBus(1)

while True:
    bus.write_byte_data(0x1D, 0x2A, 1)
    time.sleep(0.5)

    data = bus.read_i2c_block_data(0x1D, 0x00, 7)

    bus.write_byte_data(0x1D, 0x2A, 0)
    time.sleep(0.5)

    acclList = []
    for i in range(3):
        accl = (data[i+1]*256+data[i+2])/bits
        if accl > 2047:
            accl -= 4096
        acclList.append(accl)

    if len(prvList) > 0:
        if abs(acclList[0]-prvList[0])>50 or abs(acclList[2] - prvList[2])>50:
            print("Strike and Dip Measured!!")
            break
    print("Waiting")

    prvList = acclList
            
