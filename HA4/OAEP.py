import hashlib
import random

lhash = bytearray.fromhex("da39a3ee5e6b4b0d3255bfef95601890afd80709")
hLen = len(lhash)
k = 1024/8
def MGF(??):

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
def IOSP():

def DB(lhash,PS,M):
        DB = bytearray()
        DB.append(PS)
        DB.append(b'x01')
        DB.append(M)

def encode(M):
    mlen = len(M)
    psLen = (k - mLen - (2*hLen) + 2)
    ps = bytearray(psLen)
    #DB = lHash || PS || 0x01 || M
    DB = bytearray()
    DB.append(PS)
    DB.append(b'x01')
    DB.append(M)
    randOct = random.getrandbits(hlen*8)).to_bytes(hlen, byteorder='big')
    dbMask = MGF(seed,(k-hLen-1))
    maskedDB = DB ^ dbMask
    seedMask = MGF(maskedDB,hlen)
    maskedSeed = seed ^ seedMask
    EM = bytearray() #0x00 || maskedSeed || maskedDB.
    EM.append(byte(1))
    EM.append(maskedSeed)
    EM.append(maskedDB)

    return EM

def decode(EM):
    #EM = Y || maskedSeed || maskedDB
    maskedSeed = EM[1:????]
    maskedDB = EM[??:-1]

    seedMask = MGF(maskedDB,hLen)
    dbMask = MGF(seed, (k - hlen -1 ))
    DB = maskedDB ^ dbMask
    #DB = lHash' || PS || 0x01 || M


    return M
