f=open('27-A.txt')
n=int(f.readline())
m=[]
for i in range(n):
    m.append(int(f.readline()))
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if (m[i]+m[j])%3==0 and (m[i]*m[j])%4096==0:
            count+=1
print(count)