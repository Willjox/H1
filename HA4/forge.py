import string
import time
avg = 999999999
#signature = bytearray(10).tohex()
#buildingblocks = list(10)
best = 0
cur = 0
hexa = string.hexdigits[:16]
sig = list("00000000000000000000")

print(len(sig))
print(hexa)
x = hexa[0]
print(x)
input("Name: ")
input("Grade: ")
for i in range(0, 20):
    testsig = list(sig)
    for k in hexa:
        testsig[i] = k
        print("HAXXXING IN PROGRESS: ",testsig, "\r",end='')
        for z in range(0,10):
            start = time.clock()
            #WEBJOX
            stop = time.clock()
            curTime = stop - start

        if curTime > bestTime:
                bestTime = curTime
                best = k

    sig[i] = best
print("HAXXXING COMPLETE: ",sig, "\r",end='')
