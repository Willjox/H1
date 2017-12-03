i = 2
mult = 1

for j in range(1,9):
	if j !=i:
		mult = mult*j
		mult = mult/(j-i)
print(mult)
f2 = mult*2782
print(f2)


i = 4
mult = 1

for j in range(1,9):
	if j !=i:
		mult = mult*j
		mult = mult/(j-i)
print(mult)
f4 = mult*30822
print(f4)

i = 5
mult = 1

for j in range(1,9):
	if j !=i:
		mult = mult*j
		mult = mult/(j-i)
print(mult)
f5 = mult*70960
print(f5)

i = 7
mult = 1

for j in range(1,9):
	if j !=i:
		mult = mult*j
		mult = mult/(j-i)
print(mult)
f7 = mult*256422
print(f7)


f1 = 75+75+54+53+77+54+43

i = 1
mult = 1

for j in range(1,9):
	if j !=i:
		mult = mult*j
		mult = mult/(j-i)
print(mult)
f1 = mult*f1
print(f1)

secret = f1+f2+f4+f5+f7
print(secret)
