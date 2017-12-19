import binascii
import base64
import hashlib




# Found online (Stack overflow)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)
	

def long_length(number):
	l = int((len(number) / 2) // 256)
	part1 = hex(int(128 + 1 + l))[2:]
	length = hex(len(number) // 2)[2:].zfill((l +1)*2)

	return part1 + length

def der(decimal):
	number = hex(decimal)[2:]
	print("Number:",number)
	
	#Make sure the number wont be negative
	if len(bin(decimal)[2:]) % 8 == 0:
		number = "00" + number

	#Long form	
	if len(number) > 127:
		length = long_length(number)

	#Short form
	else:
		length = hex(len(number) // 2)[2:].zfill(2)
		
	return "02" + length + number

def rsa_b64(p,q,e):
	version = 0
	n = p * q
	g, x, y = egcd(e, (p - 1) * (q - 1)) # temporary
	d = x % ((p - 1) * (q - 1))
	exp1 = d % (p - 1)
	exp2 = d % (q - 1)
	g, x, y = egcd(q, p) # temporary
	coefficient = x % p

	key = der(version) + der(n) + der(e) + der(d) + der(p) + der(q) + der(exp1) + der(exp2) + der(coefficient)
	print("Key: ",key)
	length = hex(len(key) // 2)[2:]
	if len(length) %2 !=0:
		length = "0" + length
	print("Length", length)


	if len(length) > 2:
		fill_to = (len(length) // 2)
		long_def = 128 + (len(length) // 2)
		length = hex(long_def)[2:].zfill(2) + length.zfill(fill_to)
		
	print(length)

	return base64.b64encode(binascii.unhexlify("30" + length + key))





# INPUT VALUES
decimal = 161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741

p = 139721121696950524826588106850589277149201407609721772094240512732263435522747938311240453050931930261483801083660740974606647762343797901776568952627044034430252415109426271529273025919247232149498325412099418785867055970264559033471714066901728022294156913563009971882292507967574638004022912842160046962763

q = 141482624370070397331659016840167171669762175617573550670131965177212458081250216130985545188965601581445995499595853199665045326236858265192627970970480636850683227427420000655754305398076045013588894161738893242561531526805416653594689480170103763171879023351810966896841177322118521251310975456956247827719

e = 65537


#print("DER: ", der(decimal))
print("RSA: ", rsa_b64(p,q,e))




