plaintext = 'qxbxpluxvwhuzjct'
flag1=''
for char in plaintext:
    tmp = ord(char)-97
    final = (tmp+9)*9%26
    flag1+=chr(final)
print(flag1)