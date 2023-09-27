def ch(n):
    if n%2==0:
        n//=2
    else:
        n-=1
    if n%3==0:
        n//=3
    else:
        n-=1
    if n%7==0:
        n//=7
    else:
        n-=1
    return n
for n in range(1000):
    if ch(n)==1:
        print(n)


