for n in range(1,10000):
    x=n
    r=''
    while x:
        if x%2==0:
            r='1'+r
        else:
            r='0'+r
        x//=2
    r=int(r,2)
    if n-r==979:
        print(n)
        break