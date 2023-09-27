n=list(map(int, open('17.txt').readlines()))
m=10**10
for elem in n:
    if str(elem)[-1]==str(elem)[-2]:
        m=min(m,elem)
m=m**2
k=0
maxsum=0
for i in range(len(n)-1):
    if ( (str(n[i])[-1]==str(n[i+1])[-2] or str(n[i])[-2]==str(n[i+1])[-1])
    and (abs(n[i])%7==0 and abs(n[i+1])%7!=0 or abs(n[i])%7!=0 and abs(n[i+1])%7==0)
    and (n[i]**2+n[i+1]**2<=m)):
        k+=1
        maxsum=max(maxsum,n[i]**2+n[i+1]**2)
print(k,maxsum)