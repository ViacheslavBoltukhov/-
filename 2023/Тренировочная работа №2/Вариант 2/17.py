m=list(map(int, open('17.txt').readlines()))
m3=10**9
for elem in m:
    if abs(elem)%10==3:
        m3=min(m3,elem)
m3=m3**2
count=0
maxsum=0
for i in range(len(m)-1):
    if abs(min(m[i],m[i+1]))%10==3 and m[i]**2+m[i+1]**2<m3:
        count+=1
        maxsum=max(maxsum,m[i]**2+m[i+1]**2)
print(count,maxsum)