import base64

# with open("mes", "r") as f:
    # asd = f.read()
    # temp = asd
    # for i in range(20):
        # temp = base64.decode(b'HQsdFSQcABUzNgc3CCw9HhUsPgsPWwA2LlQKZ0E=')
        # print(i, temp)

temp = base64.b64decode(b'HQsdFSQcABUzNgc3CCw9HhUsPgsPWwA2LlQKZ0E=').hex()

print(temp)