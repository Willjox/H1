import hashlib

def hasher(left, right):
    return hashlib.sha1(left + right).digest()

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
        else:
            self.left = left
            self.right = right
            self.hash = hasher(self.left.getHash(),self.right.getHash());
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
        x = node('0x0','0x0',hashData(line[:-1]))
        currentDepth.append(x)

    stem.append(currentDepth)
    currentDepth = checkEven(currentDepth)
    currentDepth = climbTreeRoot(currentDepth)
    while(len(currentDepth) != 1):
        currentDepth = checkEven(currentDepth)
        stem.append(climbTree(currentDepth))
        currentDepth= stem[-1]
        print("Depth: " , len(stem))
    print("root: " , currentDepth[-1].getHash().hex())
    print(i)
    print(currentDepth)
    print(len(stem))
    leaf= stem[0][i]
    print(leaf.getHash().hex())
    k = 0
    while ((k) < (len(stem)-j)):
        leaf = leaf.getParent()
        k = k+1
    parent = leaf.getParent()
    if parent.getLeft() != leaf.getHash():
        print('L', parent.getLeft().getHash().hex())
    else:
        print('R',parent.getRight().hex())

    print(leaf)
