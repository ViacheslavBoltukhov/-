for i in range(41,100):
    n=40+2*i-1
    flag=True
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            flag=False
    if flag:
        print(i)
        break