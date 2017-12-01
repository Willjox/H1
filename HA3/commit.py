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
    currentconfidence = 100000
    results = []
    while confidence < currentconfidence:
        results.append(binding())
        avg = sum(results)/len(results)
        if len(results) > 10:
            s = stddev(results,avg)
            currentconfidence = s/(math.sqrt(len(results)))
    return avg
def binding():
    i = 0
    l = 2
    k = bytes(random.getrandbits(16))
    v = bytes(1)
    x =  hashlib.sha1(v + k).digest()[:l]
    v = bytes(2)
    y = bytes(0)
    print (x.hex())
    while x != y:
        k = bytes(random.getrandbits(16))
        y =  hashlib.sha1(v + k).digest()[:l]
        i = i + 1
        #print(i, " ",y.hex(),"\r" ,end='')

    print(i, " ",y.hex())
    return(i)


print(iterate(500))


#def concealing():
