n = int(input())
a = []
for i in range(n):
    a.append(input())
b = []
while len(a):
    if '0' in a:
        b.append(a[0:a.index('0')])
        a = a[a.index('0')+1:]
    else:
        b.append(a)
        a = []
for i in range(len(b)):
    b[i] = list(map(int, b[i]))
c = []
for i in range(len(b)):
    k = 0
    for j in range(len(b[i])):
        if b[i][j] < 0:
            k+=1
    if k!=1:
        c.append(b[i])
pmax=0
for i in range(len(c)):
    p=1
    for j in range(len(c[i])):
        p*=c[i][j]
    pmax=max(p,pmax)
print(pmax)
print(c)
            
