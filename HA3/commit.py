import random
import hashlib
import math



def stddev(results, average):
    y= []
    for x in results:
        y.append((x - average)**2)
    return math.sqrt( ( (sum(y))/len(results)) )

def iterate(confidence):
<<<<<<< HEAD

    avg = 0
    ci = 0
    s = 0
    currentconfidence = 10000
=======
    avg = 0
    ci = 0
    s = 0
    currentconfidence = 100000
>>>>>>> 971824cde6dbdcce6d43f4a9a19d119a5fb0940a
    results = []
    while confidence < currentconfidence:
        results.append(binding())
        avg = sum(results)/len(results)
        if len(results) > 10:
            s = stddev(results,avg)
            currentconfidence = s/(math.sqrt(len(results)))
<<<<<<< HEAD
            print("Confidence: ", currentconfidence)
            print(avg)

    return avg
def binding():
    rand = random.SystemRandom()
    i = 0
    l = 20
    k = bytes(rand.getrandbits(16))
=======
            print("currentconfidence: " , currentconfidence)
    return avg
def binding():
    i = 0
    l = 2
    k = bytes(random.getrandbits(16))
>>>>>>> 971824cde6dbdcce6d43f4a9a19d119a5fb0940a
    v = bytes(1)
    x =  hashlib.sha1(v + k).digest()[:l]
    v = bytes(2)
    y = bytes(0)
<<<<<<< HEAD

    while x != y:
        k = bytes(rand.getrandbits(16))
=======
    print (x.hex())
    while x != y:
        k = bytes(random.getrandbits(16))
>>>>>>> 971824cde6dbdcce6d43f4a9a19d119a5fb0940a
        y =  hashlib.sha1(v + k).digest()[:l]
        i = i + 1
        #print(i, " ",y.hex(),"\r" ,end='')

<<<<<<< HEAD
    return(i)


print(iterate(2000))
=======
    print(i, " ",y.hex())
    return(i)


print(iterate(500))
>>>>>>> 971824cde6dbdcce6d43f4a9a19d119a5fb0940a


#def concealing():
