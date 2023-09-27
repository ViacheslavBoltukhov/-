for n in range(1,1001):
    r=bin(n)[2:]
    for i in range(3):
        s=0
        x=int(r,2)
        while x:
            s+=x%10
            x//=10
        r=r+str(s%2)
    r=int(r,2)
    if r>1028:
        print(r)
        break
