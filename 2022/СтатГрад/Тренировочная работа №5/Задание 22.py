count=0
for i in range(10**8,10**9):
    a=0
    b=0
    x=i
    while x>0:
        a+=1
        d=x%10
        if d%3==0:
            b+=d
        x//=10
    if a==8 and b==66:
        count+=1
print(count)
