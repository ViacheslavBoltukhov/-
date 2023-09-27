m1=list(list(map(int, s.split(';')))for s in open('18.csv').readlines())
mmax=[[0]*20 for x in range(20)]
mmin=[[0]*20 for x in range(20)]
mmax[0][0]=m1[0][0]
for i in range(20):
    for j in range(20):
        if i==0 and j!=0:
            mmax[i][j]=mmax[i][j-1]+m1[i][j]
        elif j==0 and i!=0:
            mmax[i][j]=max(mmax[i-1][j],mmax[i-1][j+1])+m1[i][j]
        elif j!=19 and i!=0 and j!=0:
            mmax[i][j]=max(mmax[i][j-1],mmax[i-1][j-1],mmax[i-1][j],mmax[i-1][j+1])+m1[i][j]
        else:
            mmax[i][j]=max(mmax[i][j-1],mmax[i-1][j-1],mmax[i-1][j])+m1[i][j]
for i in range(20):
    print(mmax[i])
print(mmax[19][19])
mmin[0][0]=m1[0][0]
for i in range(20):
    for j in range(20):
        if i==0 and j!=0:
            mmin[i][j]=mmin[i][j-1]+m1[i][j]
        elif j==0 and i!=0:
            mmin[i][j]=min(mmin[i-1][j],mmin[i-1][j+1])+m1[i][j]
        elif j!=19 and i!=0 and j!=0:
            mmin[i][j]=min(mmin[i][j-1],mmin[i-1][j-1],mmin[i-1][j],mmin[i-1][j+1])+m1[i][j]
        else:
            mmin[i][j]=min(mmin[i][j-1],mmin[i-1][j-1],mmin[i-1][j])+m1[i][j]
for i in range(20):
    print(mmin[i])
print(mmin[19][19])