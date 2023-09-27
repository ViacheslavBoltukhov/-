n=list(map(int,open('17.txt').readlines()))
m3=10**9
for elem in n:
    if abs(elem)%10==3:
        m3=min(m3,elem)
m3=m3**2
count=0
maxsum=0
for i in range(len(n)-1):
    k3=0
    for j in range(2):
        if n[i+j]%3==0:
            k3+=1
    if abs(n[i])%10==abs(n[i+1])%10 and k3==1 and (n[i]**2+n[i+1]**2<=m3):
        count+=1
        maxsum=max(maxsum,n[i]**2+n[i+1]**2)
print(count,maxsum)
