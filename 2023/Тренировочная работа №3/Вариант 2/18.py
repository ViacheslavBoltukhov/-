f=open('18.csv').readlines()[1:]
t=[]
for elem in f:
    t.append(list(map(int, elem.split(';'))))
tmax=[[0]*20 for i in range(20)]
tmax[19][0]=t[19][0]
for i in range(1,20):
    if tmax[19][i-1]-15>=0:
        tmax[19][i]=tmax[19][i-1]-15+t[19][i]
    else:
        tmax[19][i]=0
for i in range(19)[::-1]:
    if tmax[i+1][0]-20>=0:
        tmax[i][0]=tmax[i+1][0]-20+t[0][i]
    else:
        tmax[i][0]=0
for i in range(19)[::-1]:
    for j in range(1,20):
        k1,k2,k3=0,0,0
        if tmax[i][j-1]-15>=0:
            k1=tmax[i][j-1]-15+t[i][j]
        if tmax[i+1][j-1]-10>=0:
            k2=tmax[i+1][j-1]-10+t[i][j]
        if tmax[i+1][j]-20>=0:
            k3=tmax[i+1][j]-20+t[i][j]
        tmax[i][j]=max(k1,k2,k3)
tmin=[[0]*20 for i in range(20)]
tmin[19][0]=t[19][0]
for i in range(1,20):
    if tmin[19][i-1]-15>=0:
        tmin[19][i]=tmin[19][i-1]-15+t[19][i]
    else:
        tmin[19][i]=9999
for i in range(19)[::-1]:
    if tmin[i+1][0]-20>=0:
        tmin[i][0]=tmin[i+1][0]-20+t[0][i]
    else:
        tmin[i][0]=9999
for i in range(19)[::-1]:
    for j in range(1,20):
        k1,k2,k3=0,0,0
        if tmin[i][j-1]-15>=0:
            k1=tmin[i][j-1]-15+t[i][j]
        if tmin[i+1][j-1]-10>=0:
            k2=tmin[i+1][j-1]-10+t[i][j]
        if tmin[i+1][j]-20>=0:
            k3=tmin[i+1][j]-20+t[i][j]
        tmin[i][j]=min(k1,k2,k3)
print([tmax[0][19]])
print([tmin[0][19]])