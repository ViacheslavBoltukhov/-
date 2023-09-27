for n in range(10,1001):
    x=n
    xmin=100
    xmax=0
    while x>9:
        dx=x%100
        xmin=min(xmin,dx)
        xmax=max(xmax,dx)
        x//=10
    if xmax-xmin==44:
        print(n)
        break