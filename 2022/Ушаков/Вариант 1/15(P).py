for a in range(1,100):
    if all([((not (x%12==0) or not (x%18==0)) <= (not (x%a==0))) for x in range(1,1000)]):
        print(a)
        break