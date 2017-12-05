import math
import hashlib


for x in range(1,9):
	# Creates three empty maps, zeromap to store
	# the number of occurencies of each hash
	# where the commitment is 0, onemap to store
	# the number of occurencies of each hash
	# where the commitment is 1, and one to store
	# the 
	zeromap = dict() 
	onemap = dict()
	allmap = dict()


	for k in range(0, int(math.pow(2,16))):
		hash0 = hashlib.sha256(str('0').encode('utf-8') + str(k).encode	('utf-8')).hexdigest()[0:x]
		hash1 = hashlib.sha256(str('1').encode('utf-8') + str(k).encode('utf-8')).hexdigest()[0:x]
		if hash0 in zeromap:
			zeromap[hash0]+=1
			allmap[hash0]+=1
		else:
			zeromap[hash0]=1
			if hash0 in allmap:
				allmap[hash0]+=1
			else:
				allmap[hash0]=1
		if hash1 in onemap:
			onemap[hash1]+=1
			allmap[hash1]+=1
		else:
			onemap[hash1]=1
			if hash1 in allmap:
				allmap[hash1]+=1
			else:
				allmap[hash1]=1
	print('done creating lists')
	
	#collisions
	collisions = dict()
	
	for hash in allmap:
		if allmap[hash] > 1:
			collisions[hash] = allmap[hash]

	
	#concealing
	concealed = 0
	for hash in collisions:
		if hash in zeromap:
			if zeromap[hash] != collisions[hash]:
				concealed+= collisions[hash]	
	
	#binding
	binding = math.pow(2,17) - concealed
	print("When the number of bits after truncation is ", x, " the number of concealed, or not binding, hashes are ", concealed, ". That is ", (concealed*100)/math.pow(2,17), " percent of the hashes has the concealing property. The number of binding hashes are ", int(binding),". That is ", (binding*100)/math.pow(2,17), " percent of the hashes has the binding property.")
	






	
