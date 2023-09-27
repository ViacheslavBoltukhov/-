maxsum=0
count=0
n=list(map(int, open('17.txt').read().splitlines()))
sumch=0
countch=0
for elem in n:
    if elem%2==0:
        sumch+=elem
        countch+=1
sr=sumch/countch
for i in range(1,len(n)):
    if (n[i]%3==0 or n[i-1]%3==0) and (n[i]<sr or n[i-1]<sr):
        count+=1
        maxsum=max(maxsum,n[i]+n[i-1])
print(count,maxsum)