f=open('26.txt')
n=int(f.readline())
k=[]
count=0
maxk=0
for i in range(n):
    k.append(int(f.readline()))
k=sorted(k)
for i in range(n):
    r=k[i]
    if r==0:
        continue
    count+=1
    c=1
    for j in range(i+1,n):
        if k[j]-r>=7:
            r=k[j]
            k[j]=0
            c+=1
    maxk=max(maxk,c)
print(count,maxk)