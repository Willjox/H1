import hashlib
import random
import sys
import math


def stddev(results, average):
    y= []
    for x in results:
        y.append((average - x)**2)
    return math.sqrt( ( (sum(y))/(len(results)-1) ))

def mint(u,k,c):
    bu = int(u/8)
    i = 0;
    p = 0;
    h = hashlib.md5()
    korg =  [0]*(2**u)
    rand = random.SystemRandom()

    while i < c:
        x = rand.randint(0, 2**26)
        h.update(bytes(x))
        boll = h.digest()[0:bu]
        iboll = int.from_bytes(boll,byteorder = 'big' ,signed =False)
        korg[iboll] = korg[iboll] + 1
        print("Boll: " , iboll)
        print("Bollar i korg:  " , korg[iboll])
        if  korg[iboll] == k:
            i = i + 1
            print("antal mynt: " ,i)
        p = p+1
        print(p)
    return p

k = 0
avg = 0
ci = 0
s = 0
u =int(input("u = "))
k =int(input("k = "))
c =int(input("c = "))
z =int(input("Confidence = "))

results = []
while z > ci:
    results.append((mint(u,k,c)))
    avg = sum(results)/len(results)
    if len(results) > 1:
        s = stddev(results,avg)
    ci = s/(math.sqrt(len(results)))
    print(avg)
    print(ci)
