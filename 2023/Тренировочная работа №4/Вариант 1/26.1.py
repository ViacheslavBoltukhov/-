f=open('26.txt')
n=int(f.readline())
a=[]
for elem in f:
    r,m=map(int, elem.split())
    a.append((r,m))
a=sorted(list(set(a)))
r=dict()
for i in range(len(a)):
    if a[i][0] in r:
        r[a[i][0]].append(a[i][1])
    else:
        r[a[i][0]]=[a[i][1]]
maxk=0
nr=0
for elem in r:
    m=r[elem]
    k=1
    for i in range(len(m)-1):
        if m[i+1]-m[i]-1<=7:
            k+=m[i+1]-m[i]
            if k>=maxk:
                maxk=k
                nr=elem
        else:
            k=1
print(maxk,nr)