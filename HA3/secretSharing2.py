ownPoly = [8, 4, 11, 3]
received = [sum(ownPoly), 34, 39, 39, 50]
sharedPoly = {1:sum(received), 3:2034, 4:4337, 5:7960}

result = 0

for i in sharedPoly:
	product = 1
	for j in sharedPoly:
		if i!= j:
			product *= j/(j-i)
	result += sharedPoly[i]*product

print("The deactivation code is: ", int(result))
