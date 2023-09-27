f=open('18.csv').readlines()[1:]
t=[]
for elem in f:
    t.append(list(map(int, elem.split(';'))))
tmax=[[0]*20 for i in range(20)]
tmax[19][0]=t[19][0]
for i in range(1,19):
    if tmax[19][i-1]!=0 and t[19][i-1]%2==t[19][i]%2:
        tmax[19][i]=tmax[19][i-1]+t[19][i]
for i in range(18,-1,-1):
    if tmax[i+1][0]!=0 and t[i+1][0]%2!=t[i][0]%2:
        tmax[i][0]=tmax[i+1][0]+t[i][0]
for i in range(18,-1,-1):
    for j in range(1,20):
        k1=k2=k3=0
        if tmax[i][j-1]!=0 and t[i][j]%2==t[i][j-1]%2:
            k1=tmax[i][j-1]+t[i][j]
        if tmax[i+1][j]!=0 and t[i][j]%2!=t[i+1][j]%2:
            k2=tmax[i+1][j]+t[i][j]
        if tmax[i+1][j-1]!=0:
            k3=tmax[i+1][j-1]+t[i][j]
        tmax[i][j]=max(k1,k2,k3)
k0=0
for elem in tmax:
    k0+=elem.count(0)
print(tmax[0][19],k0)