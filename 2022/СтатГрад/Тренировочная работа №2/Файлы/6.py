for i in range(1,1000000)[::-1]:
    s=i
    s=s//10
    n=1
    while s<221:
        if n%2==0:
            s=s+13
        n=n+5
    if n==101:
        print(i)
        break