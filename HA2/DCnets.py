from binascii import unhexlify, hexlify
from itertools import cycle

SA = "D75C"
SB = "EE87"

DA = "C568"
DB = "FCB3"
M = "4674"

b = 1


send=(bytes(c1 ^ c2 for c1, c2 in zip(unhexlify(SA), unhexlify(SB))).hex())

if b==0:
	A=(bytes(c1 ^ c2 for c1, c2 in zip(unhexlify(SA), unhexlify(DA))).hex())
	B=(bytes(c1 ^ c2 for c1, c2 in zip(unhexlify(SB), unhexlify(DB))).hex())
	recieve = bytes(c1 ^ c2 for c1, c2 in zip(unhexlify(A), unhexlify(B))).hex()
	send+=recieve

else:
	invert = "FFFF"
	send = (bytes(c1 ^ c2 for c1, c2 in zip(unhexlify(send), unhexlify(M))).hex())

print(send)


