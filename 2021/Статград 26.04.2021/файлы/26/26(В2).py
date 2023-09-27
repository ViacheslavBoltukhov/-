a=list(map(int, open('26.txt').read().split()))
a.pop(0)
a1=list(filter(lambda x: x%2==0,a))
a2=list(filter(lambda x: x%2==1,a))
a1.sort()
a2.sort()
smax=0
k=0
l1,l2=len(a1),len(a2)
for i in range(l1-1):
    j=i+1
    s=a1[i]+a1[j]
    while s<=a1[l1-1]:
        if s in a1:
            k+=1
            smax=max(smax,s)
        j+=1
        s=a1[i]+a1[j]
for i in range(l2-1):
    j=i+1
    s=a2[i]+a2[j]
    while s<=a1[l1-1]:
        if s in a1:
            k+=1
            smax=max(smax,s)
        j+=1
        s=a2[i]+a2[j]
print(smax,k)
