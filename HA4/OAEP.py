import hashlib
import random
import math
from binascii import unhexlify

lhash = bytearray.fromhex("da39a3ee5e6b4b0d3255bfef95601890afd80709")
hLen = len(lhash)
k = 1024/8
def MGF(seed, mlen):
    #if mlen > 32:
	 #      return "Maske length to long"
    t = bytearray()
    print(math.ceil(mlen/hLen))
    for i in range(0, math.ceil(mlen/hLen)):
        c = IOSP(i,4)

        t += hashlib.sha1(seed + c).digest()
    print(mlen)
    print("JOX",len(t[:int(mlen)]))
    return t[:int(mlen)]



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
    psLen = int((k - mLen - (2*hLen) - 2))
    PS = bytearray(psLen)
    #DB = lhash || PS || 0x01 || M
    DB  = bytearray()
    DB += lhash
    DB += PS
    DB += bytearray.fromhex("01")
    DB += M
    #GIVET? seed = random.getrandbits(hlen*8)).to_bytes(hlen, byteorder='big')
    dbMask = MGF(seed,(k-hLen-1))

    maskedDB = bytes(c1^c2 for c1, c2 in zip(unhexlify(DB.hex()), unhexlify(dbMask.hex())))

    seedMask = MGF(maskedDB,hLen)
    maskedSeed = bytes(c1^c2 for c1, c2 in zip(unhexlify(seed.hex()), unhexlify(seedMask.hex())))
    EM = bytearray()
    print(len(EM)) #0x00 || maskedSeed || maskedDB.
    EM += bytearray.fromhex("00")
    EM += maskedSeed
    print("HÄR", len(EM),len(maskedDB))
    EM += maskedDB
    return EM

def decode(EM):
    #EM = Y || maskedSeed || maskedDB
    maskedSeed = EM[1:hLen]
    maskedDB = EM[(hLen+1):]

    seedMask = MGF(maskedDB,hLen)
    dbMask = MGF(seed, (k - hLen -1 ))
    DB = bytes(c1^c2 for c1, c2 in zip(unhexlify(maskedDB.hex()), unhexlify(dbMask.hex())))                                                #maskedDB ^ dbMask
    
    for i in range(21, len(DB)):
        print(DB[i])
        if DB[i] == 1:
            M = DB[i+1:].hex()
            return M
	
#M = DB[-mLen:]
    print(M.hex())


    return M
M=bytearray.fromhex("c107782954829b34dc531c14b40e9ea482578f988b719497aa0687")
seed = bytearray.fromhex("1e652ec152d0bfcd65190ffc604c0933d0423381")
EM = bytearray.fromhex("0063b462be5e84d382c86eb6725f70e59cd12c0060f9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51efc06d40d25f96bd0f4c5d88f32c7d33dbc20f8a528b77f0c16a7b4dcdd8f")
#print((encode(M,seed).hex()))
#print((EM.hex()))
#print(len((EM.hex())))
#if decode(encode(M,seed),len(M)) == M:
#    print("yay")
print(decode(EM))

#print(MGF(bytearray.fromhex("9b4bdfb2c796f1c16d0c0772a5848b67457e87891dbc8214"), 21).hex())


