import hashlib
import random
import math

lhash = bytearray.fromhex("da39a3ee5e6b4b0d3255bfef95601890afd80709")
hLen = len(lhash)
k = 1024/8
def MGF(seed, mlen):
    #if mlen > 32:
	 #      return "Maske length to long"
    t = bytearray()
    for i in range(0, math.ceil(mlen/hLen)):
        c = IOSP(i,4)

        t += hashlib.sha1(seed + c).digest()
    print(mlen)
    return t[:int(2*mlen)]



def IOSP(x, xlen):
	x = x.to_bytes(xlen, byteorder='big')
	return x
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
    PS = bytearray(psLen)
    #DB = lhash || PS || 0x01 || M
    DB  = bytearray()
    DB += lhash
    DB += PS
    DB += b'x01'
    DB += M
    #GIVET? seed = random.getrandbits(hlen*8)).to_bytes(hlen, byteorder='big')
    dbMask = MGF(seed,(k-hLen-1))
    maskedDB = DB ^ dbMask
    seedMask = MGF(maskedDB,hlen)
    maskedSeed = seed ^ seedMask
    print(maskedDB.hex())
    print(DB.hex())
    print(seedMask.hex())
    print(maskedSeed.hex())
    EM = bytearray() #0x00 || maskedSeed || maskedDB.
    EM.append(byte(1))
    EM.append(maskedSeed)
    EM.append(maskedDB)
    print(EM.hex())
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
M=bytearray.fromhex("fd5507e917ecbe833878")
seed = bytearray.fromhex("1e652ec152d0bfcd65190ffc604c0933d0423381")
EM = bytearray.fromhex("0000255975c743f5f11ab5e450825d93b52a160aeef9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51f40e13fb29ed5101dbcb044e6232e6371935c8347286db25c9ee20351ee82")

if decode(encode(M,seed),len(M)) == M:
    print("WEEEE")
else:
    print("buu")
