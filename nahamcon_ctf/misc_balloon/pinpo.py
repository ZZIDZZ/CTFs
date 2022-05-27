strs = "}{ abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&\\'()+,-./:;<=>?@[\\]^_`|~"
numstrs = "0123456789"
for s in numstrs:  
    for st in numstrs:
        if(int(s)+int(st) == int(s)*int(st)):
            print(s, st, int(s)+int(st), int(s)*int(st))