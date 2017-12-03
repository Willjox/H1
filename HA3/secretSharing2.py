ownPoly = [9, 19, 5]
received = [sum(ownPoly), 37, 18, 40, 44, 28]
sharedPoly = {1:sum(received), 4:1385, 5:2028}

result = 0

for i in sharedPoly:
	product = 1
	for j in sharedPoly:
		if i!= j:
			product *= j/(j-i)
	result += sharedPoly[i]*product

print("The deactivation code is: ", int(result))
