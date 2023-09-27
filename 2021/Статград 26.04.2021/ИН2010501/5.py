for x in range(1,1000):
    n=x
    if n%2==0: n//=2
    else: n-=1
    if n%3==3: n//=3
    else: n-=1
    if n%5==0: n//=5
    else: n-=1
    if n==1: print(x)
