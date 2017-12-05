import random
import hashlib
import math
from bitarray import bitarray



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
        results.append(binding(16))
        avg = sum(results)/len(results)
        if len(results) > 10:
            s = stddev(results,avg)
            currentconfidence = s/(math.sqrt(len(results)))
            print("Confidence: ", currentconfidence)
            print(avg)

    return avg

def binding(l):

    rand = random.SystemRandom()
    k = (rand.getrandbits(16)).to_bytes(2, byteorder='big')
    commit = bitarray()
    commit.frombytes(k)
    commit.append(True)

    lb = (l//8) + 1
    strip = l%8


    x = hashlib.sha1(commit.tobytes()).digest()[:lb]
    xb = bitarray()
    xb.frombytes(x)
    while xb.length() > l:
        xb.pop(-1)
    x = xb.tobytes()
    print(x.hex())
    i = 0
    y = bytearray()




    print(x.hex())
    while x != y:
        k = (rand.getrandbits(16)).to_bytes(2, byteorder='big')
        commit = bitarray()
        commit.frombytes(k)
        commit.append(False)
        y = hashlib.sha1(commit.tobytes()).digest()[:lb]
        yb = bitarray()
        yb.frombytes(y)
        while yb.length() > l:
            yb.pop(-1)
        y = yb.tobytes()
        i = i + 1
        #print(i, " ",y.hex(),x.hex(), yb,xb, "\r",end='')
    print(i)
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
        return(i)

print(iterate(500))
