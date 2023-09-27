n=15*1728**8+9*144**12+7*12**12+154
r=''
while n:
    if n%12==10:
        r+='A'
    elif n%12==11:
        r+='B'
    else:
        r+=str(n%12)
    n//=12
r=r[::-1]
print(r)
print(r.count('0'))