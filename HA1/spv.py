import hashlib

l = (b'')
r = (b'')
h = hashlib.sha1()
with open('path') as fp:
     t = fp.readline()[:-1]
     prev = bytearray.fromhex(t)

     for line in fp:
         pos, line = line[:1], line[1:-1]
         print(line)
         hexToByte = bytearray.fromhex(line)

         if pos == 'R':
             r = hexToByte
             l = prev
         else:
             l = hexToByte
             r = prev

         h.update(l+r)
         prev = h.digest()
         h = hashlib.sha1()
     print('Root: ',prev.hex())
