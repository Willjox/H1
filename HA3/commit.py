import random
import hashlib
import math



def stddev(results, average):
    y= []
    for x in results:
        y.append((x - average)**2)
    return math.sqrt( ( (sum(y))/len(results)) )

def iterate(confidence):
    avg = 0
    ci = 0
    s = 0
    currentconfidence = 10000
    avg = 0
    ci = 0
    s = 0
    currentconfidence = 100000
    results = []
    while confidence < currentconfidence:
        results.append(binding())
        avg = sum(results)/len(results)
        if len(results) > 10:
            s = stddev(results,avg)
            currentconfidence = s/(math.sqrt(len(results)))
            print("Confidence: ", currentconfidence)
            print(avg)

    return avg
def binding():
    rand = random.SystemRandom()
    i = 0
    l = 20
    k = bytes(random.getrandbits(16))
    v = bytes(1)
    x =  hashlib.sha1(v + k).digest()[:l]
    v = bytes(2)
    y = bytes(0)

    while x != y:
        k = bytes(rand.getrandbits(16))
        y =  hashlib.sha1(v + k).digest()[:l]
        i = i + 1
        #print(i, " ",y.hex(),"\r" ,end='')
    return(i)

def concealing():
        rand = random.SystemRandom()
        i = 0
        l = 20
        k = bytes(random.getrandbits(16))
        v = bytes(1)
        x =  hashlib.sha1(v + k).digest()[:l]
        v = bytes(2)
        y = bytes(0)

        while x != y:
            k = bytes(rand.getrandbits(16))
            y =  hashlib.sha1(v + k).digest()[:l]
            i = i + 1
            #print(i, " ",y.hex(),"\r" ,end='')
        return(i)

print(iterate(500))
