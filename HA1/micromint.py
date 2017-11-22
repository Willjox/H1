import random
import sys
import math


def stddev(results, average):
    y= []
    for x in results:
        y.append((x - average)**2)
    return math.sqrt( ( (sum(y))/z) )

def mint(u,k,c):
    i = 0;
    p = 0;
    korg =  [0]*(2**u)
    rand = random.SystemRandom()
    while p < c:
        x = rand.randint(0, len(korg)-1)
        if korg[x] <= k:
            korg[x] +=1
            if korg[x] == k:
                p+=1
        i+=1
    return i

k = 0
avg = 0
ci = 0
s = 0
u =int(input("u = "))
k =int(input("k = "))
c =int(input("c = "))
z =int(input("Number of itterations = "))

results = []
i=0
while i<z:
    results.append((mint(u,k,c)))
    i+=1
    print(i)
avg = sum(results)/len(results)
s = stddev(results,avg)
ci = 2*3.66*s/(math.sqrt(z))
print(avg)
print(ci)
