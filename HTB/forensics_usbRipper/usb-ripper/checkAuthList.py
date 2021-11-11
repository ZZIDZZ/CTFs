import os

checked = []
auth_list = open("auth.json","r")
auth_list = auth_list.read()
k = 0
numCheck = ""


for i in range (1,5):
    syslog = open("syslog", "r")
    for j in syslog:
        if k%9==0:
            k=0
        elif k==5:
            numCheck = j[67::].rstrip()
            if numCheck not in checked:
                checked.append(numCheck)
                if numCheck not in auth_list:
                    print(f"found unauthorized manufacturer: {numCheck}")
        k+=1
