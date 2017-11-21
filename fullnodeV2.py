import hashlib

def hasher(left, right):
    return hashlib.sha1(left.getHash() + right.getHash()).digest()

def hashData(data):
    byteData = bytearray.fromhex(data)
    return byteData

def checkEven(list):
    if len(list)%2 != 0:
        list.append(list[-1])
    return list

def climbTree(base):
    parents = []
    temp = list(base)
    while(len(temp) != 0):
        left = temp.pop(0)
        right = temp.pop(0)
        parent = node(left,right,'0x0')
        left.adopt(parent)
        right.adopt(parent)
        parents.append(parent)

    return parents
def climbTreeRoot(base):
    parents = []
    temp = list(base)
    while(len(temp) != 0):
        left = node('0x0','0x0',temp.pop(0))
        right = node('0x0','0x0',temp.pop(0))
        parent = node(left,right,'0x0')
        left.adopt(parent)
        right.adopt(parent)
        parents.append(parent)
    return parents

class node:
    def __init__(self, left, right,hash):
        if (left == '0x0'):
            self.hash = hash
            return

        self.left = left
        self.right = right
        self.hash = hasher(left,right);
        self.parent = self

    def adopt(self,parent):
        self.parent = parent
    def getHash(self):
        return self.hash
    def getParent(self):
        return self.parent
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left

currentDepth = []
stem = []

with open('leaves') as fp:
    i = int(fp.readline())
    j = int(fp.readline())

    for line in fp:
        if line == '':
            break
        currentDepth.append(hashData(line[:-1]))

    stem.append(currentDepth)
    currentDepth = checkEven(currentDepth)
    currentDepth = climbTreeRoot(currentDepth)
    while(len(currentDepth) != 1):
        currentDepth = checkEven(currentDepth)
        stem.append(climbTree(currentDepth))
        currentDepth= stem[-1]
        print("Depth: " , len(stem))
    print("root: " , currentDepth[-1].getHash().hex())



node = stem[-1][-1]
div = 2**(len(stem)-1)
depth = 0
right = 1
while div >=2:
	if  int(i/div) == 0:
		node = node.left
	else:
		node = node.right
		i = i-div
	depth = depth + 1
	div= int(div/2)
	print(node.hash.hex())
if i%2 ==0:
	node = node.left
else:
	node = node.right
depth = depth+1
print(node.hash.hex())

merkletree = ''
right = 0
print("Printing the Merkle tree: ")
while depth >= 2:
	if node.parent.parent.getLeft().getHash() == node.parent.getHash():
		node = node.parent.parent.getRight()
		right = 1
	else:
		node = node.parent.parent.getLeft()
		right = 0
	depth = depth -1
	if depth ==j:
		if right == 1:
			merkletree+='R'
		else:
			merkletree+='L'
		merkletree+=node.hash.hex()
		merkletree+= stem[-1][-1].hash.hex()
		print("This is the node at depth j: ")
	print(node.hash.hex())
print(merkletree)


