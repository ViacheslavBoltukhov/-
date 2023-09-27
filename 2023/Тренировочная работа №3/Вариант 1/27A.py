f=open('27-A.txt')
n=int(f.readline())
k=0
m=[int(f.readline()) for i in range(n)]
for i in range(n-18):
    for j in range(i+17,n):
        if (m[i]+m[j])%8==0 and m[i]*m[j]%2187==0:
            k+=1
print(k)