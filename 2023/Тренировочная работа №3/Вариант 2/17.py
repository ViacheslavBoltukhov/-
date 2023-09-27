n=list(map(int, open('17.txt').readlines()))
m7=10**9
for elem in n:
    if abs(elem)%10==7:
        m7=min(m7,elem)
m7=m7**2
count=0
maxsum=0
for i in range(len(n)-1):
    k7=0
    for j in range(2):
        if n[i+j]%7==0:
            k7+=1
    if abs(n[i])%10==abs(n[i+1])%10 and k7==1 and (n[i]**2+n[i+1]**2)<=m7:
        count+=1
        maxsum=max(maxsum,n[i]**2+n[i+1]**2)
print(count,maxsum)

