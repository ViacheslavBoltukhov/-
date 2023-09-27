f=open('27-B.txt')
n=int(f.readline())
m=[[0]*13 for i in range(3)]
count=0
for i in range(n):
    x=int(f.readline())
    x2=x
    k2=0
    while x2%2==0:
        k2+=1
        x2//=2
        if k2==12:
            break
    for j in range(12-k2,13):
        count+=m[(3-x%3)%3][j]
    m[x%3][k2]+=1
print(count)