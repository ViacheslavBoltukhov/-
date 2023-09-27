for i in range(1,1000):
    n=i
    r=''
    while n:
        r+=str(n%2)
        n//=2
    r=r[::-1]
    if i%2==0:
        r+='01'
    else:
        r+='10'
    r=int(r,2)
    if r>81:
        print(r)
        break