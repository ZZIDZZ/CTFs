import struct
import pwn 
import socket
import time

payload1 = "\x5a\x65\x72\x6f\x73\x20\x26\x20\x4f\x6e\x65\x73"
payload2 = "\x4f\x68\x20\x77\x6f\x77\x77\x77\x21\x20\x42\x61\x73\x65\x20\x31\x30\x20\x69\x73\x20\x63\x6f\x6f\x6c\x20\x61\x6e\x64\x20\x61\x6c\x6c\x20\x62\x75\x74\x20\x48\x65\x78\x78\x78\x78"
payload3 = "\x57\x65\x20\x63\x61\x6E\x20\x72\x65\x70\x72\x65\x73\x65\x6E\x74\x20\x6E\x75\x6D\x62\x65\x72\x73\x20\x69\x6E\x20\x61\x6E\x79\x20\x62\x61\x73\x65\x20\x77\x65\x20\x77\x61\x6E\x74"
payload4 = "\x54\x68\x69\x73\x20\x69\x73\x20\x6f\x6e\x65\x20\x62\x69\x67\x20\x27\x6f\x6c\x20\x69\x6e\x74\x65\x67\x65\x72\x21"
payload5 = "Bases on bases on bases on bases :)"
payload6 = "\x49\x74\x27\x73\x20\x67\x6f\x6f\x64\x20\x74\x6f\x20\x6b\x6e\x6f\x77\x20\x74\x68\x65\x20\x64\x69\x66\x66\x65\x72\x65\x6e\x63\x65\x20\x3a\x29"
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
clientSocket.connect(("challenge.nahamcon.com",31958))
clientSocket.send(payload1.encode())
time.sleep(1)
dataFromServer = clientSocket.recv(4096)
print(dataFromServer.decode())
clientSocket.send(payload2.encode())
time.sleep(1)
dataFromServer = clientSocket.recv(4096)
print(dataFromServer.decode())
clientSocket.send(payload3.encode())
time.sleep(1)
dataFromServer = clientSocket.recv(4096)
print(dataFromServer.decode())
clientSocket.send(payload4.encode())
time.sleep(1)
dataFromServer = clientSocket.recv(4096)
print(dataFromServer.decode())
clientSocket.send(payload5.encode())
time.sleep(1)
dataFromServer = clientSocket.recv(4096)
print(dataFromServer.decode())
clientSocket.send(payload6.encode())
time.sleep(1)
dataFromServer = clientSocket.recv(4096)
print(dataFromServer.decode())
