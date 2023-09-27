for i in range(1000):
    n=i
    r=''
    while n:
        r+=str(n%2)
        n//=2
    r=r[::-1]
    for j in range(2):
        if r.count('1')%2==1:
            r+='1'
        else:
            r+='0'
    if int(r,2)>77:
        print(i)
        break
