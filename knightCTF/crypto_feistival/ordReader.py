ct = open('cipher.txt', 'rb').read()
dec = ""

for chars in ct:
    dec+=f"{chars}, "

print(dec)