import string
import time
import urllib.request
avg = 999999999
#signature = bytearray(10).tohex()
#buildingblocks = list(10)
best = 0
cur = 0
hexa = string.hexdigits[:16]
sig = list("00000000000000000000")
bestTime = 0
def buildurl(name,sig,grade):
    return "http://eitn41.eit.lth.se:3119/ha4/addgrade.php?name={}&grade={}&signature={}".format(name,grade,"".join(sig))

print(len(sig))
print(hexa)
x = hexa[0]
print(x)
name = input("Name: ")
grade = input("Grade: ")
for i in range(0, 20):
    testsig = list(sig)
    for k in hexa:
        testsig[i] = k
        print("HAXXXING IN PROGRESS: ","".join(testsig), "\r",end='')
        for z in range(0,10):
            start = time.clock()
            http = buildurl(name,testsig,grade)
            print (http)
            with urllib.request.urlopen(http) as response:
                stop = time.clock()
                curTime = curTime + (stop-start)
            print(curTime)
            print("najs")

        if curTime > bestTime:
                bestTime = curTime
                best = k

    sig[i] = best
print("HAXXXING COMPLETE: ","".join(sig))
