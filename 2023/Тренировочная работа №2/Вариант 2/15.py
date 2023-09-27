for a in range(-1000,1000):
    flag=True
    for x in range(1,1000):
        for y in range(1,1000):
            if not(((108%x==0)<=(x%y!=0)) or (x+y>80) or (a-y>x)):
                flag=False
                break
        if not flag:
            break
    if flag:
        print(a)
        break