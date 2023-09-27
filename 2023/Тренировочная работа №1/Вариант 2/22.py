f=list(list(map(str, s.split(';'))) for s in open('22.csv').readlines())
t=[0]*len(f)
print(f)
for i in range(len(f)):
    if f[i][2]=='':
        t[i]=int(f[i][1])
    else:
        if f[i][2].count(':')>0:
            p=list(map(int, f[i][2].split(':')))
        else:
            p=[int(f[i][2])]
        for elem in p:
            for j in range(len(f)):
                if int(f[j][0])==elem:
                    t[i]=max(int(f[i][1])+t[j]+5,t[i])
print(max(t))