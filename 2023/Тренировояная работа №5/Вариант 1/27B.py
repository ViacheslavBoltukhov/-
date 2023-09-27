f=open('27-B.txt')
n=int(f.readline())
ost=[[0]*9 for i in range(9)]
k=0
for i in range(n):
    x=int(f.readline())
    for j in range(9):
        k+=ost[j][(i-x-j)%9]
    ost[x%9][i%9]+=1
print(k%10**6)