for x in range(37):
    n=3*37**3+1*37**2+7*37+x+4*37**3+x*37**2+2*37+9
    if n%36==0:
        print(n//36)
        break