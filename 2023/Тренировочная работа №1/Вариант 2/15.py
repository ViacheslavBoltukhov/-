for a in range(1000):
    flag=True
    for x in range(1,1000):
        if not( ((72%x==0)<=(90%x!=0)) or (a-x>80) ):
            flag=False
            break
    if flag:
        print(a)
        break