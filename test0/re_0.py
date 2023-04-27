string0 = 'GMBH|Xfmd1nf`u1`uif`xpsme`pg`Sfwfstf~'
flag = ''
for char in string0:
    flag += chr(ord(char) - 1)
    print(chr(ord(char) - 1))
print(flag)

string1 = 'qxbxpluxvwhuzjct'
flag1 = ''
for char in string1:
    tmp = (ord(char)) - 97
    final = (tmp - 7)
    flag1 += chr((ord(char) - 97 - 7) * 9 % 26 + 97)

print(flag1)
