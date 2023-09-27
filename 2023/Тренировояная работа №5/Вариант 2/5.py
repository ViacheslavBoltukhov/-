for n in range(1000000,0,-1):
    r=bin(n)[2:]
    if n%5==0:
        r+='101'
    else:
        r+='1'
    if int(r,2)%7==0:
        r+='111'
    else:
        r+='1'
    r=int(r,2)
    if r<1855663:
        print(n)
        break

