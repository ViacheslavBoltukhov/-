for i in range(-1000,1000):
    s=i
    s=(s-10)//7
    n=1
    while s>0:
        n*=2
        s-=n
    if n==8:
        print(i)
        break
