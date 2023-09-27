s,n=map(int, open('26.txt').readline().split())
a=sorted([int(elem) for elem in open('26.txt').readlines()[1:]])
i=0
while a[i]<=s:
    s-=a[i]
    i+=1
else:
    m=i
    while s-a[m+1]+a[i]>=0:
        m+=1
print(i,a[m])

