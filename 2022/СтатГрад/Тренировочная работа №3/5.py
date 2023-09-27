for x in range(2,10000):
    n=bin(x)[2:]
    k1=0
    k0=0
    for i in range(1,len(n),2):
        k1+=int(n[i])
    for i in range(0,len(n),2):
        if n[i]=='0':
            k0+=1
    if abs(k1-k0)==5:
        print(x)
        break