x=int('521111111',9)
a=1
b=0
while x>0:
    d=x%9
    a*=d
    if d<5:
        b+=d
    x//=9
print(a,b)