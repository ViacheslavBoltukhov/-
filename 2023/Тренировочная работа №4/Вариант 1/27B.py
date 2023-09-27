f=open('27-B.txt')
n=int(f.readline())
a=[[0]*9 for i in range(9)]
def d2(n):
    k=0
    while n%2==0:
        k+=1
        n//=2
        if k>7:
            return 8
    return k
def d5(n):
    k=0
    while n%5==0:
        k+=1
        n//=5
        if k>7:
            return 8
    return k
k=0
for elem in f:
    x=int(elem)
    k2,k5=d2(x),d5(x)
    if k2<=7 and k5<=7:
        k+=a[7-k2][7-k5]
    if k2<=7:
        for i in range(8-k5,9):
            k+=a[7-k2][i]
    if k5<=7:
        for i in range(8-k2,9):
            k+=a[i][7-k5]
    a[k2][k5]+=1
print(k)