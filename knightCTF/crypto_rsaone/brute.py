from curses import raw
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from base64 import b64decode

from numpy import little_endian

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])
words = b"}{ abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&\\'()+,-./:;<=>?@[\\]^_`|~"
for word in words:
    with open('flag.enc', 'rb') as raw_ct:
        try:
            ct = raw_ct.read()
            key = open('private.pem', "rb").read()
            replaced = key[:136] + word.to_bytes(1, 'little') + key[136+1:]
            # print(replaced)
            rsa_key = RSA.importKey(replaced)
            cipher = PKCS1_v1_5.new(rsa_key)
            raw_cipher_data = b64decode(ct)
            phn = cipher.decrypt(raw_cipher_data)
            print(phn)
        except Exception as e:
            print(e)

