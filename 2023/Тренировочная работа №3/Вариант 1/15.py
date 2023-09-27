for a in range(101):
    flag=True
    for x in range(1001):
        if not( ((x&35!=0) or (x&22!=0)) <= ((x&15==0)<=(x&a!=0)) ):
            flag=False
            break
    if flag:
        print(a)
        break