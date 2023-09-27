for i in range(1,1000):
    x=i
    l,m=94,0
    while l>=x:
        m+=1
        l-=x
    if m<l:
        x=m
        m=l
        l=x
    if l==3 and m==7:
        print(i)
        break