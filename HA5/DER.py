
import binascii

def der(decimal):
	bytes = decimal.to_bytes((decimal.bit_length() + 7) // 8, byteorder='big')
	number = str(binascii.hexlify(bytes))[2:-1].zfill(2)

	if len(bin(decimal)[2:]) % 8 == 0:
		number = "00" + number
		
	if len(number) > 127:
		length = int((len(number)/2) // 256)
		first = int(128+1+length)
		fill = (length +1)*2
		bytes2 = (len(number)//2).to_bytes(((len(number)//2).bit_length() + 7) // 8, byteorder='big')
		len_hex = str(binascii.hexlify(bytes2)//2)[2:-1].lstrip("0").zfill(fill)
		byteshex = first.to_bytes((first.bit_length() + 7) // 8, byteorder='big')
		hex = str(binascii.hexlify(byteshex))[2:-1]
		return "02" + hex + len_hex + number

	bytes2 = (len(number)//2).to_bytes(((len(number)//2).bit_length() + 7) // 8, byteorder='big')
	len_hex = str(binascii.hexlify(bytes2))[2:-1].lstrip("0").zfill(2)

	return "02" + len_hex + num_hex

	


decimal = 161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741

print("DER: ", der(decimal))


