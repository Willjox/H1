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
    while(len(base) != 0):
        left = base.pop(0)
        right = base.pop(0)
        parent = node(left.getHash(),right.getHash(),'0x0')
        left.adopt(parent)
        right.adopt(parent)
        parents.append(parent)

    return parents
def climbTreeRoot(base):
    parents = []
    while(len(base) != 0):
        left = node('0x0','0x0',base.pop(0))
        right = node('0x0','0x0',base.pop(0))
        parent = node(left.getHash(),right.getHash(),'0x0')
        left.adopt(parent)
        left.adopt(parent)
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
        currentDepth = climbTree(currentDepth)
        stem.append(currentDepth)
        print("Depth: " , len(stem))
    print("root: " , currentDepth[-1].getHash().hex())
    print(i)
    print(currentDepth)
    print(len(stem))
    leaf= stem[2][-1]
    k = 0
    while ((k-1) > j):
        leaf = leaf.getParent()
        k = k+1
    parent = leaf.getParent()
    if parent.getLeft() != leaf.getHash():
        print('L', parent.getLeft().Hex()
              )
    else:
        print('R',parent.getRight().hex())

    print(leaf)
