x=729**6-3**20+90
s=''
while x:
    s+=str(x%9)
    x//=9
print(s.count('0'))
