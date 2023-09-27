a=list(map(int, open('26.txt').read().split()))
a.pop(0)
a1=list(filter(lambda x: x%2==0,a))
a2=list(filter(lambda x: x%2==1,a))
a1.sort()
a2.sort()
smax=0
k=0
l1,l2=len(a1),len(a2)
for i in range(l1):
    j=0
    s=a1[i]+a2[j]
    while s<=a2[l2-1]:
        if s in a2:
            k+=1
            smax=max(smax,s)
        j+=1
        s=a1[i]+a2[j]
print(smax,k)
