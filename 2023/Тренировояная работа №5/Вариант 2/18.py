f=open('18.csv').readlines()[1:]
t=[]
for elem in f:
    t.append(list(map(int, elem.rstrip().split(';'))))
tmax=[[0]*15 for i in range(15)]
tmin=[[0]*15 for i in range(15)]
tmax[14][0]=t[14][0]
tmin[14][0]=t[14][0]
for i in range(14,-1,-1):
    for j in range(15):
        if i==14 and j==0:
            continue
        elif i==14:
            tmax[i][j]+=tmax[i][j-1]+abs(t[i][j-1]-t[i][j])
            tmin[i][j]+=tmin[i][j-1]+abs(t[i][j-1]-t[i][j])
        elif j==0:
            tmax[i][j]+=tmax[i+1][j]+abs(t[i+1][j]-t[i][j])
            tmin[i][j]+=tmin[i+1][j]+abs(t[i+1][j]-t[i][j])
        else:
            tmax[i][j]+=max(tmax[i+1][j]+abs(t[i+1][j]-t[i][j]),tmax[i][j-1]+abs(t[i][j-1]-t[i][j]))
            tmin[i][j]+=min(tmin[i+1][j]+abs(t[i+1][j]-t[i][j]),tmin[i][j-1]+abs(t[i][j-1]-t[i][j]))
print(tmin[0][14],tmax[0][14])