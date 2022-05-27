import string

ALPHABET = 'abcdefghijklmnop'

# splits every characters in pt (8 bits) to 2 characters (4 & 4 bits) used as index
# to map to alphabet
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - 97
	t2 = ord(k) - 97
	return ALPHABET[(t1 + t2) % 16]

flag = "redacted"
key = "a"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
for asd in ALPHABET:
	enc = ""
	for i, c in enumerate(b16):
		enc += shift(c, asd[i % len(asd)])
	print(asd, enc)

# key: j