for a in range(1001):
    if all((((x&116!=0) or (x&92!=0))<=((x&69==0)<=(x&a!=0))) for x in range(1001)):
        print(a)
        break