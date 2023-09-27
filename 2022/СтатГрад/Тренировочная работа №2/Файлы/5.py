for n in range(1,1000000):
    s1=0
    s2=0
    x=n
    while x:
        if x%2==0:
            s1+=x%10
        x//=10
    x=str(n)
    for i in range(1,len(x),2):
        s2+=int(x[i])
    if abs(s1-s2)==9:
        print(n)
        break