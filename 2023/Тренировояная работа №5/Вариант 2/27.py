f=open('27-A.txt')
n=int(f.readline())
m=[]
for i in range(n):
    m.append(int(f.readline()))
k=0
for i in range(n-1):
    for j in range(i+1,n):
        if (j-i)%7==(m[i]+m[j])%7:
            k+=1
print(k)
'''-------------'''
f=open('27-B.txt')
n=int(f.readline())
ost=[[0]*7 for i in range(7)]
k=0
for i in range(n):
    x=int(f.readline())
    for j in range(7):
        k+=ost[j][(i-x-j)%7]
    ost[x%7][i%7]+=1
print(k%10**6)