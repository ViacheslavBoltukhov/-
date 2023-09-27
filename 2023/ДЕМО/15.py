for a in range(1,1001):
    for x in range(1,1000):
        flag=True
        if not(((x%2==0)<=(x%3!=0)) or(x+a>=100)):
            flag=False
            break
    if flag:
        print(a)
        break
