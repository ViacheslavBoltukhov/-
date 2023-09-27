n=list(map(int, open('17.txt').readlines()))
m3=-9993
count=0
maxsum=0
for elem in n:
    if elem>m3 and abs(elem)%10==3:
        m3=elem
m3=m3**2
for i in range(len(n)-1):
    if (abs(n[i])%10==3 and abs(n[i+1])%10!=3) or (abs(n[i])%10!=3 and abs(n[i+1])%10==3):
        if n[i]**2+n[i+1]**2>=m3:
            count+=1
            maxsum=max(maxsum,n[i]**2+n[i+1]**2)
print(count,maxsum)
