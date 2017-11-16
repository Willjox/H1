import hashlib

l = (b'')
r = (b'')
h = hashlib.sha1()
with open('path') as fp:
     prev = int(fp.readline()[:-1],16).to_bytes(20, byteorder='big', signed='False')
     print(prev.hex())
     for line in fp:
         if line == '':
             break
         line = line[:-1]
         pos, line = line[:1], line[1:]
         print(line)
         print(line[:-1])
         i = int(line[2:],16).to_bytes(20, byteorder='big', signed='False')
         if pos == 'R':
             print(i.hex, "HÖGER")
             r = i
             l = prev
         else:
             l = i
             r = prev
             print(i, "VÄNSTER")

         h.update(l)
         h.update(r)
         prev = h.digest()
     print('Root: ',prev.hex())
