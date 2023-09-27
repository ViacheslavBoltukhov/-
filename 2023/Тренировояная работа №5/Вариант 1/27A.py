f=open('27-A.txt')
n=int(f.readline())
m=[]
for i in range(n):
    m.append(int(f.readline()))
k=0
for i in range(n-1):
    for j in range(i+1,n):
        if (j-i)%9==(m[i]+m[j])%9:
            k+=1
print(k)