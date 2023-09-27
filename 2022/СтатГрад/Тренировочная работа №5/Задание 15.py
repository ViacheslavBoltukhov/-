for a in range(51):
    flag=True
    for x in range(51):
        for y in range(51):
            if not( (x**2+y**2<a) or (x>3) or (y>=5) ):
                flag=False
                break
    if flag:
        print(a)
        break