f=open('26.txt')
n=int(f.readline())
a=set()
for elem in f:
    r,m=map(int, elem.split())
    a.add((r,m))
a=sorted(a)
r=[[],[]]
k=1
for i in range(len(a)-1):
    d=a[i+1][0]-a[i][0]-1
    if d>0:
        for j in range(d):
            r.append([])
            k+=1
    if a[i][0]==a[i+1][0]:
        r[k].append(a[i][1])
    else:
        r[k].append(a[i][1])
        r.append([])
        k+=1
maxk=0
nr=0
for elem in r:
    k=1
    for i in range(len(elem)-1):
        if elem[i+1]-elem[i]<=9:
            k+=elem[i+1]-elem[i]
            if k>maxk:
                maxk=k
                nr=r.index(elem)
        else:
            k=1
print(maxk,nr)
