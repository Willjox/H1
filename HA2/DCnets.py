from binascii import unhexlify, hexlify
from itertools import cycle

SA = "27C2"
SB = "0879"

DA = "35F6"
DB = "1A4D"
M = "27BC"

b = 1


send=(bytes(c1 ^ c2 for c1, c2 in zip(unhexlify(SA), unhexlify(SB))).hex())
if b==0:
	A=(bytes(c1 ^ c2 for c1, c2 in zip(unhexlify(SA), unhexlify(DA))).hex())
	B=(bytes(c1 ^ c2 for c1, c2 in zip(unhexlify(SB), unhexlify(DB))).hex())
	recieve = bytes(c1 ^ c2 for c1, c2 in zip(unhexlify(A), unhexlify(B))).hex()
	send+=recieve
else:
	invert = "FFFF"
	M = (bytes(c1 ^ c2 for c1, c2 in zip(unhexlify(send), unhexlify(M))).hex())
	M = (bytes(c1 ^ c2 for c1, c2 in zip(unhexlify(invert), unhexlify(M))).hex())

print(send)


