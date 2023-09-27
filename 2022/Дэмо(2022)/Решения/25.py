count=0
x=700000
while count!=5:
    m=0
    d=2
    while x%d!=0 and d<x//2+1:
        d+=1
    else:
        m=d+x//d
        if m%10==8:
            count+=1
            print(x,m)
    x+=1
