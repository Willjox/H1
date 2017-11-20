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
        parent = node(left.getHash(),right.getHash())
        parents.append(parent)

    return parents
def climbTreeRoot(base):
    parents = []
    while(len(base) != 0):
        left = base.pop(0)
        right = base.pop(0)
        parent = node(left,right)
        parents.append(parent)
    return parents

class node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.hash = hasher(left,right);

    def adopt(parent):
        self.parent = parent
    def getHash(self):
        return self.hash


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
