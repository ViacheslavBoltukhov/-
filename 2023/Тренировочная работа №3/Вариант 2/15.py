for a in range(1001):
    flag=True
    for x in range(1001):
        if not( ((x&42!=0) or (x&13!=0))<=((x&30==0)<=(x&a!=0))  ):
            flag=False
            break
    if flag:
        print(a)
        break