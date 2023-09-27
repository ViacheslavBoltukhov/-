for  k in int(bin(987654321)[2:-3],2), int(bin(2123456789)[2:-3],2):
    for n in range(k-10,k+10):
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
        if r>=987654321 and k==int(bin(987654321)[2:-3],2):
            mink=k1
            break
        elif r>2123456789 and k==int(bin(2123456789)[2:-3],2):
            kmax=k1-1
            break
print(kmax-mink+1)

