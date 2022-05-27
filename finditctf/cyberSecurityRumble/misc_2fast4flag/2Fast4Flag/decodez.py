import os

file = open('challenge.log', 'r')
text = file.readlines()
checked =[]
for line in text:
    text.append(line.rstrip())
    pass
for line in text:
    asd = 0
    for check in checked:
        if check == line: asd+=1
        if asd>=5: break

    if asd<3:
        print(f"detected unidentified id: {line}")

# print(os.getcwd())
# with open('challenge.log', 'r') as file:
    # text = file.read()
    # for line in text:
        # hexCode = str(line[9::].rstrip())
        # print(hexCode)