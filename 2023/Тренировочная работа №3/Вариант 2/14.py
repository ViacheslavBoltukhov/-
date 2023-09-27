for p in range(10,21):
    for x in range(p):
        for y in range(p):
            if x*p**3+x*p**2+x*p+8+4*p**3+3*p**2+x*p+9==y*p**3+y*p**2+4:
                print(y*p**2+y*p+x)