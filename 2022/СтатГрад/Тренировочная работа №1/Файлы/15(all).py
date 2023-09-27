for a in range(1000):
    if all([(x&85==0)<=((x&54!=0)<=(x&a!=0)) for x in range(1000)]):
        print(a)
        break
