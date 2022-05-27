import string

cts = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"
ALPHABET = 'abcdefghijklmnop'
REALALPHABET = string.printable
clue = cts[0:8]
def rev_b16(a,b):
    ad =  int("".join([i for i in [bin(ALPHABET.index(a))[2:].zfill(4), bin(ALPHABET.index(b))[2:].zfill(4)]]), 2)
    return chr(ad)

def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc

def shift(c, k):
    t1 = ord(c) - 97
    return ALPHABET[(t1 + 9) % 16]

def rev_shift(c, ks = "j"):
    k = ord(ks) - 97
    dec = ""
    for i in c:
        if chr(ALPHABET.index(i) - k + 97) not in ALPHABET:
            dec += chr(ALPHABET.index(i) - k + 97 + 16)
        else:
            dec += chr(ALPHABET.index(i) - k + 97)
    return dec

for asd in ALPHABET:
    reved = rev_shift(cts, asd)
    dec = ""
    for i in range(0, len(reved), 2):
        dec += rev_b16(reved[i], reved[i+1])
    print(asd, dec)
