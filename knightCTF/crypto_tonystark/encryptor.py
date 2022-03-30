secret = input("Enter your string to encrypt: ")
secarr = []
x = 1

"""IihsIb_7[^7is<inH][l_^D`Ib_;[n7iu"""
"""IihsIb_7ad7is<inH][l_^D`Ib_;[n7iu"""

origin = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C"
,"D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

enc = ["[","\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","v","6","7","8","9"
,":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Q"]

keys = ["T3NR1NG$","T3nR1ng$","TenRings","T3nR!ngs","T3nR!ng$","73NR1GN$","73nRing$","T3nR!nG$"]


def secretfucn(secret,secarr,x):
    for character in secret:
        secarr.append(ord(character))
    for i in range(len(secarr)):
        if 97 <= secarr[i] <= 122:
            secarr[i] = secarr[i]-6
        elif 65 <= secarr[i] <= 90:
            secarr[i] = secarr[i]-11
    x = x + 1
    if x % 2 == 0:
        secarr[i] = secarr[i] + 3
    else:
        secarr[i] = secarr[i] + 2
    encrypted = ""
    for val in secarr:
        encrypted = encrypted + chr(val)
    print("Encrypted Text: " + encrypted)

for k in range(10):
    secretfucn(secret,secarr,k)
    secarr = []
