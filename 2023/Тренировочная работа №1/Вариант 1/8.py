count=0
for x in range(int('1000000',9),int('10000000',9)):
    k6=0
    knch=0
    n=x
    while n:
        if n%9==6:
            k6+=1
        if (n%9)%2==1:
            knch+=1
        n//=9
    if k6==1 and knch==2:
        count+=1
print(count)