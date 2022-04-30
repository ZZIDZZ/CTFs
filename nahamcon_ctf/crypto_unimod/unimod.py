import random

flag = open('flagtest', 'r').read()
ct = ''
k = random.randrange(0,65533)
print(k)
for c in flag:
    print(ord(c))
    kkk = ord(c) + k
    print(kkk, kkk%65533)
    ct += chr((ord(c) + k) % 65533)

open('out', 'w').write(ct)
