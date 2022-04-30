cts = "饇饍饂饈饜餕饆餗餙饅餒餗饂餗餒饃饄餓饆饂餘餓饅餖饇餚餘餒餔餕餕饆餙餕饇餒餒饞飫"

# for c in flag:
#   ct += chr((ord(c) + k) % 65533)
k = 0
for i in range(0,65533):
    if chr(ord(cts[0]) - i) == "f":
        k = i
        break

flag = "".join([chr(ord(ct) - k) for ct in cts])
print(flag)