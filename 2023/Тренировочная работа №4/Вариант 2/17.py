n=list(map(int, open('17.txt').readlines()))
m=10**10
for elem in n:
    if abs(elem)%10==abs(elem)%100//10:
        m=min(m,elem)
m=m**2
def f1(a,b):
    return abs(a)%10==abs(b)%100//10 or abs(b)%10==abs(a)%100//10
def f2(a,b):
    return a%13==0 and b%13!=0 or b%13==0 and a%13!=0
k=0
maxsum=0
for i in range(len(n)-1):
    if f1(n[i],n[i+1]) and f2(n[i],n[i+1]) and n[i]**2+n[i+1]**2<=m:
        k+=1
        maxsum=max(maxsum,n[i]**2+n[i+1]**2)
print(k,maxsum)