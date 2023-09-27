m1=list(list(map(int, s.split(';'))) for s in open('18.csv').readlines())
mmax=[[0]*20 for x in range(20)]
mmin=[[0]*20 for x in range(20)]
for i in range(20)[::-1]:
    for j in range(20):
        if i==19 and j==0:
            mmax[i][j]=m1[i][j]
        elif i==19 and j!=0:
            mmax[i][j]=mmax[i][j-1]+m1[i][j]
        elif j==0 and i!=19:
            mmax[i][j]=max(mmax[i+1][j],mmax[i+1][j+1])+m1[i][j]
        elif j!=19 and i!=19 and j!=0:
            mmax[i][j]=max(mmax[i][j-1],mmax[i+1][j-1],mmax[i+1][j],mmax[i+1][j+1])+m1[i][j]
        else:
            mmax[i][j]=max(mmax[i][j-1],mmax[i+1][j-1],mmax[i+1][j])+m1[i][j]
print(mmax[0][19])
for i in range(20)[::-1]:
    for j in range(20):
        if i==19 and j==0:
            mmin[i][j]=m1[i][j]
        elif i==19 and j!=0:
            mmin[i][j]=mmin[i][j-1]+m1[i][j]
        elif j==0 and i!=19:
            mmin[i][j]=min(mmin[i+1][j],mmin[i+1][j+1])+m1[i][j]
        elif j!=19 and i!=19 and j!=0:
            mmin[i][j]=min(mmin[i][j-1],mmin[i+1][j-1],mmin[i+1][j],mmin[i+1][j+1])+m1[i][j]
        else:
            mmin[i][j]=min(mmin[i][j-1],mmin[i+1][j-1],mmin[i+1][j])+m1[i][j]
print(mmin[0][19])