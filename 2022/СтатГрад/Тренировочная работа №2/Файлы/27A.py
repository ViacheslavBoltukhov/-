numbs=list(map(int, open('27-A.txt').read().splitlines()))
n=numbs[0]
numbs.pop(0)
maxs=0
for i in range(n-1):
    for j in range(i+1,n):
        s=0
        count=0
        for k in range(i,j+1):
            if numbs[k]%2==0 and numbs[k]>0:
                count+=1
            s+=numbs[k]
        if count%30==0:
            maxs=max(s,maxs)
print(maxs)