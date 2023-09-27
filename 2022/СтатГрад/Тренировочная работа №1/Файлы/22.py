from math import gcd
for i in range(1,100):
    x=i
    a=7*x+27
    b=7*x-33
    if gcd(a,b)==15:
        print(i)
        break
