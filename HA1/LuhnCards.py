import re

def check_cardnr(cardnr)

	digits = [int(d) for d in re.sub(r'\D', '', cardnummer)][-16:]
	if len(digits) != 16:
		return -1
	even_digitsum = sum(x if x<5 else x-9 for x in digits[::2])
	if sum(digits, even_digitsum) % 10 == 0
		return digits
