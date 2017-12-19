import binascii
import base64
import hashlib


def int_to_str(decimal):
	bytes = decimal.to_bytes((decimal.bit_length() + 7) // 8, byteorder='big')
	return str(binascii.hexlify(bytes))[2:-1]

# from stack overflow
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)
	

def long_def_form(number):
	len_bytes = int((len(number) / 2) // 256)
	first = int(128 + 1 + len_bytes)
	fill_to = (len_bytes + 1) * 2
	len_hex = int_to_str(len(number) // 2).lstrip("0").zfill(fill_to)
	first_hex = int_to_str(first)
		
	return "02" + first_hex + len_hex + number

def der(decimal):
	number = int_to_str(decimal).zfill(2)
	
	if len(bin(decimal)[2:]) % 8 == 0:
		number = "00" + number
		
	if len(number) > 127:
		return long_def_form(number)
	
	#print(len(num_hex) // 2)
	
	len_hex = int_to_str(len(number) // 2).lstrip("0").zfill(2)
		
	return "02" + len_hex + number

def rsa_b64(p,q,e):
	n = p * q
	g, x, y = egcd(e, (p - 1) * (q - 1)) # temporary
	d = x % ((p - 1) * (q - 1))
	e1 = d % (p - 1)
	e2 = d % (q - 1)
	g, x, y = egcd(q, p) # temporary
	coeff = x % p

	key = der(0) + der(n) + der(e) + der(d) + der(p) + der(q) + der(e1) + der(e2) + der(coeff)
	length = int_to_str(len(key) // 2)

	if len(length) > 2:
		fill_to = (len(length) // 2)
		long_def = 128 + (len(length) // 2)
		length = int_to_str(long_def).zfill(2) + length.zfill(fill_to)
		
	print(length)

	return base64.b64encode(binascii.unhexlify("30" + length + key))

def rsa(p,q,e= 65537):
	n = p * q
	g, x, y = egcd(e, (p - 1) * (q - 1)) # temporary
	d = x % ((p - 1) * (q - 1))
	e1 = d % (p - 1)
	e2 = d % (q - 1)
	g, x, y = egcd(q, p) # temporary
	coeff = x % p

	key = der(0) + der(n) + der(e) + der(d) + der(p) + der(q) + der(e1) + der(e2) + der(coeff)
	length = int_to_str(len(key) // 2)

	if len(length) > 2:
		fill_to = (len(length) // 2)
		long_def = 128 + (len(length) // 2)
		length = int_to_str(long_def).zfill(2) + length.zfill(fill_to)
		
	print(length)

	return "30" + length + key


def find_private(p,q,identity):
	m =p*q
	i = 0
	while i!=1:
		hashvalue = hashlib.sha1(identity)
		identity = hashvalue.digest()
		a = int(binascii.hexlify(identity),16)
		i = jacobi(a,m)
	exp = (m + 5 - p + q) // 8
	r = pow(a, exp, m)
	return r

def jacobi(a, m):
	j = 1
	a %= m
	while a:
		t = 0
		while not a & 1:
			a >>= 1
			t += 1
		if t & 1 and m % 8 in (3, 5):
			j = -j
		if a % 4 == m % 4 == 3:
			j = -j
		a, m = m % a, a
	return j if m == 1 else 0

# INPUT VALUES
decimal = 161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741

p = int("9240633d434a8b71a013b5b00513323f",16)
q = int("f870cfcd47e6d5a0598fc1eb7e999d1b", 16)

e = 65537

identity ="walterwhite@crypto.sec".encode("utf-8")
#encryptedbits =

print("DER: ", der(decimal))
print("RSA: ", rsa_b64(p,q,e))
print("Priv key: ", find_private(p,q,identity))




