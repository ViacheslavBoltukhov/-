f=open('27-A.txt')
n=int(f.readline())
a=[int(f.readline()) for i in range(n)]
k=0
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]*a[j]%10**7==0 and a[i]*a[j]%10**8!=0:
            k+=1
print(k)