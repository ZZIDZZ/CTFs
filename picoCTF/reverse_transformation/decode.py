flagTxt = open('enc', 'r')
flagTxt = flagTxt.read()

msg = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽"
flag = ''.join([chr((ord(flagTxt[i]) >> 8) + ord(flagTxt[i + 1])) for i in range(len(flagTxt), 0, -2)])
print(flag)