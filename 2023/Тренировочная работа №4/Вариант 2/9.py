f=open('09.csv')
k=0
n=[]
c=[]
c_over=[]
for elem in f:
    s=list(sorted(map(int, elem.split(';'))))
    n.append(s)
    c.append([])
    for i in range(len(s)):
        c[k].append(s.count(s[i]))
    k+=1
l=len(c)
k=0
for i in range(l):
    c_over.append([])
    for j in range(len(n[i])):
        count=0
        x=n[i][j]
        a=n[:i]+n[i+1:]
        for elem in a:
            count+=elem.count(x)
        c_over[k].append(count)
    k+=1
print(c_over)
k=0
numb=0
for e1 in c_over:
    if 50 in e1:
        ind=e1.index(50)
        if c[numb][ind]==1:
            k+=1
    numb+=1
print(k)
