def f(n):
    r=bin(n)[2:]
    if int(r,2)%5==0:
        r+='101'
    else:
        r+='1'
    if int(r,2)%7==0:
        r+='111'
    else:
        r+='1'
    return int(r,2)
for n in range(1728404,1,-1):
    if f(n)<1728404:
        print(n)
        break