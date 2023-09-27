for n in range(10,10001):
    x=n
    a=[]
    while x>9:
        a.append(x%100)
        x//=10
    if max(a)+min(a)==137:
        print(n)
        break