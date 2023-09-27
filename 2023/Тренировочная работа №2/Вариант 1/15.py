for a in range(-100000,1000):
    flag=True
    for x in range(1,1000):
        for y in range(1,1000):
            if not( ((144%x==0)<=(x%y!=0)) or (x+y>100) or (a-x>y) ):
                flag=False
                break
        if not flag:
            break
    if flag:
        print(a)
        break