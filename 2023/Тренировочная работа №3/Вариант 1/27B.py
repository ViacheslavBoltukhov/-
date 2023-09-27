f=open('27-B.txt')
n=int(f.readline())
k=0
m=[[0]*8 for i in range(8)]
r=[int(f.readline()) for i in range(18)]
def d3(n):
    d=0
    while n%3==0:
        d+=1
        n//=3
    if d>=7:
        return 7
    return d
for i in range(18,n):
    x=int(f.readline())
    r.append(x)
    m[r[0]%8][d3(r[0])]+=1
    r.pop(0)
    for j in range(7-d3(x),8):
        k+=m[(8-x%8)%8][j]
print(k)