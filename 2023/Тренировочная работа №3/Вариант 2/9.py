f=open('09.csv')
k=0
for elem in f:
    s=list(sorted(map(int, elem.split(';'))))
    p=[]
    n=[]
    for i in range(len(s)):
        if s.count(s[i])==1:
            n.append(s[i])
        else:
            p.append(s[i])
    if len(p)!=0 and len(n)!=0:
        if sum(n)/len(n)<sum(p)/len(p):
            k+=1
print(k)