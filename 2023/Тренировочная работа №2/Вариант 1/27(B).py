f=open('27-B.txt')
k=int(f.readline())
n=[[0]*9 for i in range(4)]
s=0
for i in range(k):
    x=int(f.readline())
    k3=0
    k4=x%4
    while x%3==0:
        k3+=1
        x//=3
        if k3==8:
            break
    s+=sum(n[(4-k4)%4][8-k3:])
    n[k4][k3]+=1
print(s)