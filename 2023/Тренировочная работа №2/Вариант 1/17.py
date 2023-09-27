n=list(map(int, open('17.txt').readlines()))
x5=10001
for elem in n:
    x5=min(x5,elem)
x5=x5**2
count=0
maxsum=0
for i in range(len(n)-1):
    if abs(min(n[i],n[i+1]))%10==5 and n[i]**2+n[i+1]**2<x5:
        count+=1
        maxsum=max(maxsum,n[i]**2+n[i+1]**2)
print(count,maxsum)