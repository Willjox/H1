import hashlib
import random
import math
from binascii import hexlify, unhexlify

lhash = "da39a3ee5e6b4b0d3255bfef95601890afd80709"
hLen = len(lhash)
k = 1024/8
def MGF(seed, mlen):
    if mlen > 2**32:
	      return "Mask length to long"
    t = ""
    print(mlen/hLen)
    for i in range(0, math.ceil(mlen/hLen)):
        c = IOSP(i,4)
        print(i)
        print(c)
        print(seed)
        print(hashlib.sha1(bytearray.fromhex(seed + c)).hexdigest())
        t += hashlib.sha1(bytearray.fromhex(seed + c)).hexdigest()
        print(t)
    print(mlen)
    return t[:int(2*mlen)]



def IOSP(x, xlen):
	return hex(x)[2:].zfill(xlen)
  # 1.  If maskLen > 2^32 hLen, output "mask too long" and stop.
  #
  # 2.  Let T be the empty octet string.
  #
  #3.  For counter from 0 to \ceil (maskLen / hLen) - 1, do the
  #   following:

  #   A.  Convert counter to an octet string C of length 4 octets (see
  #           Section 4.1):
  #
                #C = I2OSP (counter, 4) .
#
#       B.  Concatenate the hash of the seed mgfSeed and C to the octet
#           string T:
#
#              T = T || Hash(mgfSeed || C) .
#
#  4.  Output the leading maskLen octets of T as the octet string mask.

def encode(M,seed):
    mLen = len(M)
    psLen = int((k - mLen - (2*hLen) + 2))
    PS = IOSP(0, psLen)
    #DB = lhash || PS || 0x01 || M
    DB  = ""
    DB += lhash
    DB += PS
    DB += "01"
    DB += M
    print(DB)
    #GIVET? seed = random.getrandbits(hlen*8)).to_bytes(hlen, byteorder='big')
    print(k-hLen-1)
    dbMask = MGF(seed,(k-hLen-1))
    maskedDB = bytes(c1^c2 for c1, c2 in zip(unhexlify(DB), unhexlify(dbMask))).hex()
    print(maskedDB)
    seedMask = MGF(maskedDB,hLen)
    maskedSeed = bytes(c1^c2 for c1, c2 in zip(unhexlify(seed), unhexlify(seedMask))).hex()
    print(maskedDB)
    print(DB)
    print(seedMask)
    print(maskedSeed)
    #EM = "" #0x00 || maskedSeed || maskedDB.
    #EM.append(byte(1))
    #EM.append(maskedSeed)
    #EM.append(maskedDB)
    EM = IOSP(0,1) + maskedSeed + maskedDB
    print(EM)
    return EM

def decode(EM,mLen):
    #EM = Y || maskedSeed || maskedDB
    maskedSeed = EM[1:hlen]
    maskedDB = EM[(hLen+1):-1]
    print(maskedDB.hex())
    print(maskedSeed.hex())
    seedMask = MGF(maskedDB,hLen)
    dbMask = MGF(seed, (k - hlen -1 ))
    print(seedMask.hex())
    print(dbMask.hex())
    DB = maskedDB ^ dbMask
    M = DB[-mLen:]
    print(M.hex())


    return M
M = "fd5507e917ecbe833878"
seed = "1e652ec152d0bfcd65190ffc604c0933d0423381"
EM = "0000255975c743f5f11ab5e450825d93b52a160aeef9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51f40e13fb29ed5101dbcb044e6232e6371935c8347286db25c9ee20351ee82"
print(encode(M,seed))
print(EM)
#if encode(M,seed) == EM:
#	print("yay")
#else:
#	print("FAIL")
#if decode(encode(M,seed),len(M)) == M:
 #   print("WEEEE")
#else:
 #   print("buu")
