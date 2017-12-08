avg = 999999999
#signature = bytearray(10).tohex()
#buildingblocks = list(10)
best = 0
cur = 0

for i in range(0, 1):
    for k in range (0, 256):
            for z in range (0, 1):
                byteblock = k.to_bytes(1,byteorder='big')
                print (byteblock.hex())
            #if bestTime < curTime:
            #    bestTime = curTime
            #    best = cur
