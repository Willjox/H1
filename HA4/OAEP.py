import hashlib
import random

lhash = bytearray.fromhex("da39a3ee 5e6b4b0d 3255bfef 95601890 afd80709")
hLen = len(lhash)
k = 1024/8
def MGF(??):

def encode(M):
    mlen = len(M)
    psLen = (k - mLen - (2*hLen) + 2)
    ps = bytearray(psLen)
    #DB = lHash || PS || 0x01 || M
    randOct = random.getrandbits(hlen*8)).to_bytes(hlen, byteorder='big')
    dbMask = MGF(seed,(k-hLen-1))
    #maskedDB = DB \XOR dbMask
    seedMask = MGF(maskedDB,hlen)
    #maskedSeed = seed \xor seedMask
    #EM = 0x00 || maskedSeed || maskedDB.
    return EM

def decode(EM):
    #EM = Y || maskedSeed || maskedDB
    seedMask = MGF(maskedDB,hLen)
    dbMask = MGF(seed, (k - hlen -1 ))
    #DB = maskedDB \xor dbMask
    #DB = lHash' || PS || 0x01 || M
    return M
