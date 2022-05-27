from dataclasses import replace


def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

file = open('private.pem', 'rb')
key = file.read()
print(key)
replaced = key[:136] + b'0' + key[136+1:]
print(replaced)
