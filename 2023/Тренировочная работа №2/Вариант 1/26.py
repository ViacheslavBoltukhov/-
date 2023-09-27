f=open('26.txt')
m=[]
for elem in f:
    l,col=map(str, elem.split())
    m.append([int(l),col])
m.sort(reverse=True)
k=0
maxcount=0
count=1
for i in range(len(m)-1):
    l=m[i][0]
    col=m[i][1]
    if l==0:
        continue
    for j in range(i+1,len(m)):
        if m[j][0]==0:
            continue
        if l-m[j][0]>=5 and col!=m[j][1]:
            count+=1
            l=m[j][0]
            col=m[j][1]
            m[j][0]=0
    maxcount=max(maxcount,count)
    count=1
    k+=1
print(k,maxcount)
