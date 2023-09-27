f=list(list(map(str, s.split(';'))) for s in open('22.csv').readlines()[1:])
tb=[]
m=0
for elem in f:
    tb.append(int(elem[1]))
    m=max(m,int(elem[0]))
t=[0]*(m+1)
for elem in f:
    if elem[2]=='0':
        t[int(elem[0])]=int(elem[1])
    else:
        if elem[2][0]=='"':
            t1=int(elem[2][1:])
            t2=int(elem[3][:-2])
        else:
            t1=int(elem[2])
            t2=0
        t[int(elem[0])]=max(t[t1],t[t2])+int(elem[1])
t=[x for x in filter(lambda i: i!=0,t)]
tn=[]
for i in range(len(tb)):
    tn.append(t[i]-tb[i])
k=0
for elem in tn:
    if elem>100:
        k+=1
print(k)