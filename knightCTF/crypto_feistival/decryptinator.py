from xml.dom.minidom import Notation
def enc(plain):
    L, R = plain[0:len(plain)//2], plain[len(plain)//2:]
    x = "".join(chr(ord(f(R, m)[i]) ^ ord(L[i])) for i in range(len(L)))
    y = f(R, 0)

    L, R = y, x
    x = "".join(chr(ord(f(R, n)[i]) ^ ord(L[i])) for i in range(len(L)))
    y = f(R, 0)
    ciphertext = x + y
    return ciphertext

origin = "}{ abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&\\'()+,-./:;<=>?@[\]^_`|~"
encOrd = [126, 120, 35, 98, 97, 96, 103, 102, 101, 100, 107, 106, 105, 104, 111, 110, 109, 108, 115, 114, 
113, 112, 119, 118, 117, 116, 123, 122, 121, 51, 50, 49, 48, 55, 54, 53, 52, 59, 58, 66, 65, 64, 71, 70, 
69, 68, 75, 33, 36, 126, 56, 58, 56, 62, 32, 34, 32, 46, 40, 42, 40, 46, 32, 34, 32, 70, 64, 66, 64, 61, 
60, 68, 74, 68, 71, 67, 8, 10, 8, 28, 26, 28, 30, 28, 18, 108, 15, 11, 11, 15, 15, 51, 46, 35]
ct = [72, 64, 87, 69, 120, 101, 102, 106, 112, 119, 102, 111, 1, 53, 40, 35, 6, 22, 2, 35, 0, 21, 7, 4]
dec = ""
notAvail = ""
for char in ct:
    if char in encOrd:
        dec+=origin[encOrd.index(char)]
    else:
        dec+="(.)"
        try:
            notAvail+=chr(char)
            for i in range(255):
                if enc(i) in encOrd:
                    dec+=enc(i)
        except:pass
print(dec)
print(notAvail)

m, n = 21, 22
def f(word, key):
    out = ""
    for i in range(len(word)):
        out += chr(ord(word[i]) ^ key)
    return out
