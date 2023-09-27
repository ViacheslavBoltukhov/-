for p in range(7,50):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if (y*p**2+4*p+y)+(y*p**2+6*p+5)==(x*p**3+z*p**2+3*p+3):
                    print(x*p**2+y*p+z)
                    exit()