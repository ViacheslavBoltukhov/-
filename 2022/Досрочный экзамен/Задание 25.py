for x in range(10):
    for y in range(10):
        n=int('12345'+str(x)+'6'+str(y)+'8')
        if n%17==0:
            print(n,n//17)