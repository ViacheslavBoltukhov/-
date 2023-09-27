for p in range(5,50):
    for x in range(p):
        for y in range(p):
            if (1*p+2)*(3*p+4)==x*p**2+y*p+2:
                print(y*p+x)
                exit()