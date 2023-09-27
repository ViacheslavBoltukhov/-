f=open('26.txt')
m=[]
for elem in f:
    l,col=map(str, elem.split())
    m.append([int(l),col])
m.sort()
count=1
maxcount=0
k=0
for i in range(len(m)-1):
    l=m[i][0]
    col=m[i][1]
    if l==0:
        continue
    for j in range(i+1,len(m)):
        if m[j][0]==0:
            continue
        if m[j][0]-l>=7 and m[j][1]!=col:
            count+=1
            l=m[j][0]
            m[j][0]=0
            col=m[j][1]
    maxcount=max((count,maxcount))
    k+=1
    count=1
print(k,maxcount)