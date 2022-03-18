a=[67,111,109,112,97,114,51,95,116,104,101,95,99,104,52,114,97,99,116,51,114,0]
b=[]
for i in range(0,len(a)):
    print(chr(a[i]))
    b.append(chr(a[i]))
c=str(''.join(b))
print(c)
