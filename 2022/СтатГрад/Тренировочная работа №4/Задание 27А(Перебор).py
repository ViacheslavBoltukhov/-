numbs=list(map(int, open('27-A.txt').readlines()))
n=numbs[0]
numbs.pop(0)
count=0
for i in range(100,n-1):
    s=sum(numbs[i-100:i])
    for j in range(i,n):
        s+=numbs[j]
        if s%999==0:
            count+=1
print(count)