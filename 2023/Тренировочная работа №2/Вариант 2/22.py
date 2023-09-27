f=list(list(map(str, s.split(';')[:-1])) for s in open('22.csv').readlines()[1:])
m=0
for elem in f:
    m=max(m,int(elem[0]))
t=[0]*(m+1)
for elem in f:
    if elem[2]=='0':
        t[int(elem[0])]=int(elem[1])
    else:
        if elem[2][0]=='"':
            t1=int(elem[2][1:])
            t2=int(elem[3][:-1])
        else:
            t1=int(elem[2])
            t2=0
        t[int(elem[0])]+=max(t[t1],t[t2])+int(elem[1])
count=0
for elem in t:
    if elem!=0 and elem<=120:
        count+=1
print(count)