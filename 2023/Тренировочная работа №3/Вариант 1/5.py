k=int(bin(123456789)[2:-3],2)
for n in range(k-10,k+11):
    r=bin(n)[2:]
    k1=int(r,2)
    for i in range(3):
        s=0
        x=int(r,2)
        while x:
            s+=x%10
            x//=10
        r+=str(s%2)
    r=int(r,2)
    if r>=123456789:
        print(k1,r)
        break
k=int(bin(1987654321)[2:-3],2)
for n in range(k-10,k+11)[::-1]:
    r=bin(n)[2:]
    k2=int(r,2)
    for i in range(3):
        s=0
        x=int(r,2)
        while x:
            s+=x%10
            x//=10
        r+=str(s%2)
    r=int(r,2)
    if r<=1987654321:
        print(k2,r)
        break
print(k2-k1+1)