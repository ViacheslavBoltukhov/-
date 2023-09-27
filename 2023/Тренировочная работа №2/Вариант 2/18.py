f=open('18.csv')
m=[]
for elem in f:
    m.append(list(map(int, elem.split(';'))))
n=[[0 for i in range(22)] for j in range(22)]
for i in range(1,21)[::-1]:
    for j in range(1,21):
        n[i][j]+=max(n[i][j-1],n[i-1][j],n[i+1][j+1],n[i+1][j-1])+m[i][j]
print(n[1][20])
e=[[0 for i in range(22)] for j in range(22)]
e[1][20]=1
count=m[1][20]%2
for i in range(1,21):
    for j in range(1,21)[::-1]:
        if n[i][j]+m[i-1][j+1]==n[i-1][j+1]:
            e[i][j]+=e[i-1][j+1]
        if n[i][j]+m[i+1][j]==n[i+1][j]:
            e[i][j]+=e[i+1][j]
        if n[i][j]+m[i-1][j-1]==n[i-1][j-1]:
            e[i][j]+=e[i-1][j-1]
        if n[i][j]+m[i][j+1]==n[i][j+1]:
            e[i][j]+=e[i][j+1]
        if e[i][j]==1:
            count+=m[i][j]%2
print(count)