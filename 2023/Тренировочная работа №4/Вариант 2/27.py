f=open('27-B.txt')
n=int(f.readline())
def d2(n):
    k=0
    while n%2==0:
        k+=1
        n//=2
        if k>6:
            return 7
    return k
def d5(n):
    k=0
    while n%5==0:
        k+=1
        n//=5
        if k>6:
            return 7
    return k
a=[[0]*8 for i in range(8)]
count=0
for elem in f:
    x=int(elem)
    k2,k5=d2(x),d5(x)
    if k2<=6 and k5<=6:
        count+=a[6-k2][6-k5]
    if k2<=6:
        for i in range(7-k5,8):
            count+=a[6-k2][i]
    if k5<=6:
        for i in range(7-k2,8):
            count+=a[i][6-k5]
    a[k2][k5]+=1
print(count)
