import hashlib
import random
#u =int(input("u = "))
#k =int(input("k = "))
#c =int(input("c = "))

def mint(u,k,c):
    bu = int(u/8)
    i = 0;
    p = 0;
    h = hashlib.md5()
    korg =  [0]*(2**u)
    random.seed()

    while i < c:
        x = random.getrandbits(28)
        h.update(bytes(x))
        boll = h.digest()[0:bu]
        iboll = int.from_bytes(boll,byteorder = 'big' ,signed =False)
        korg[iboll] = korg[iboll] + 1
        #print("Boll: " , iboll)
        #print("Bollar i korg:  " , korg[iboll])
        if  korg[iboll] == k:
            i = i + 1
            #print("antal mynt: " ,i)
        p = p+1
        #print(p)
    return p

k = 0
while k < 10:
    print(mint(16,2,1))
    k = k+1
