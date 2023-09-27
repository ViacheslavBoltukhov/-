for i in range(1,100)[::-1]:
    s=i
    n= 1024
    while s >= 5:
        s = s - 5
        n = n // 2
    if n==64:
        print(i)
        break
