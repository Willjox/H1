import re


def check_cardnr(cardnr):
	pos = cardnr.index('X')
	digits = [int(d) for d in re.sub(r'\D', '0', cardnr)][0:16]
	even_digitsum = sum(x if x<5 else x-9 for x in digits[::2])
	subtract = (sum(digits, even_digitsum))% 10
	replace = (10-subtract)%10
	if pos%2==0:
		if replace%2==0:
			replace = int(replace/2)
		else:
			replace = int((replace+9)/2)
	return str(replace)


result = ''
with open('cards2') as fp:
	for line in fp:
		append = check_cardnr(line)
		result+=append
print(result)
