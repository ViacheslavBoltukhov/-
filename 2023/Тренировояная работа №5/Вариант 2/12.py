for n in range(49,100):
    s=48+2*n-1
    flag=True
    for d in range(2,int(s**0.5)+1):
        if s%d==0:
            flag=False
            break
    if flag:
        print(n)
        break