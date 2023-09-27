n=list(map(int, open('17.txt').readlines()))
k7=10**9
for elem in n:
    if abs(elem)%10==7 and elem<k7:
        k7=elem
k7=k7**2
count=0
maxsum=0
for i in range(len(n)-1):
    if (abs(n[i])%10==7 and abs(n[i+1])%10!=7) or (abs(n[i])%10!=7 and abs(n[i+1])%10==7):
        if n[i]**2+n[i+1]**2<k7:
            count+=1
            maxsum=max(maxsum,n[i]**2+n[i+1]**2)
print(count,maxsum)