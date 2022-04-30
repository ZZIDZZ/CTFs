flagTxt = open('enc', 'r')
flagTxt = flagTxt.read()

msg = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽"
output = ''

# for i in range(len(flagTxt), 0, 2):
    # output += ''.join(chr((ord(flagTxt[i]) << 8) + ord(flagTxt[i + 1])))

# flag = ''.join([chr((ord(flagTxt[i]) >> 8) + ord(flagTxt[i + 1])) for i in range(len(flagTxt), 0, -2)])
# print(flag)

for i in range(len(flagTxt), 0, 2):
    print(((ord(flagTxt[i]) - ord(flagTxt[i + 1])) >> 8), i)
    # try:
    #     output += ''.join(chr((ord(flagTxt[i]) - ord(flagTxt[i + 1])) >> 8))
    # except:
    #     pass

# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

print(output)