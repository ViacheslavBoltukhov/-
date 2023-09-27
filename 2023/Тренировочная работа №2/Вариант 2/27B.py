f=open('27-B.txt')
n=int(f.readline())
m=[[0 for i in range(11)] for j in range(100)]
s=0
for i in range(n):
    x=int(f.readline())
    k4=x%100
    k3=0
    while x%3==0:
        k3+=1
        x//=3
    if k4%4==0:
        for j in range(0,len(m),4):
            s+=sum(m[j][10-k3:])
    else:
        for j in range(4-k4%4,len(m),4):
            s += sum(m[j][10 - k3:])
    m[k4][k3]+=1
print(s)



