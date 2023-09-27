'''Файл А
f=open('27-A.txt')
n=int(f.readline())
m=[]
for i in range(n):
    m.append(int(f.readline()))
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if (m[i]+m[j])%4==0 and (m[i]*m[j])%6561==0:
            count+=1
print(count)'''
'''Файл В'''
f=open('27-B.txt')
n=int(f.readline())
m=[[0]*9 for i in range(4)]
count=0
for i in range(n):
    x=int(f.readline())
    k4=x%4
    k3=0
    while x%3==0:
        k3+=1
        x//=3
        if k3==8:
            break
    count+=sum(m[(4-k4)%4][8-k3:])
    m[k4][k3]+=1
print(count)