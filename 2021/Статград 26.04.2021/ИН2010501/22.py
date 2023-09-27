for x in range(1,100):
    a=3*x+23
    b=3*x-17
    if a*b>0:
        while a!=b:
            if a>b: a-=b
            else: b-=a
        if a==20:
            print(x)
            break
