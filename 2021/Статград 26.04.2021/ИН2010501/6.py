'''for x in range(1,1000):
    for s in range(1,1000):
        chislo=100*s+x
        n=1
        while chislo<2021:
            chislo=chislo+5*n
            n+=1
        if n==15:
            print(x,s)
            exit(0)'''
s = int(input())
x = int(input())
s = 100*s + x
n = 1
while s < 2021:
    s = s + 5*n
    n = n + 1
    print(s)
print(n)
