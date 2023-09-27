f=open('26.txt')
n=int(f.readline())
p=[]
for i in range(n):
    r,m=f.readline().split()
    p.append([int(r),int(m)])
p=sorted(p)
l=1
k=0
kmax=0
nr=0
for i in range(1,len(p)):
    if p[i][0]==p[i-1][0]:
        if p[i][1]==p[i-1][1]:
            continue
        elif p[i][1]-1==p[i-1][1]:
            l+=1
        else:
            if l>=3:
                k+=1
            l=1
    else:
        if l>=3:
            k+=1
        l=1
        if k>=kmax:
            kmax=k
            nr=p[i][0]-1
        k=0
print(kmax,nr)