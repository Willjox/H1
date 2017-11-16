import hashlib

l = (b'')
r = (b'')
h = hashlib.sha1()
with open('path') as fp:
     prev = (fp.readline()) #[:-1]

     for line in fp:
         if line == '':
             break
         #line = line[:-1]
         pos, line = line[:1], line[1:]
         if pos == 'R':
             print(line, "HÖGER")
             r = line.encode('ascii')
             l = prev.encode('ascii')
         else:
             l = line.encode('ascii')
             r = prev.encode('ascii')
             print(line, "VÄNSTER")

         h.update(l)
         h.update(r)

         prev = h.hexdigest()
     print('Root: ',prev)
