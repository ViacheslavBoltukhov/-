f=list(map(int, open('17.txt').readlines()))
m5=10**10
k=0
maxsum=0
for e in f:
    s=str(e)
    if len(s)==3 and s[-1]=='5':
        m5=min(m5,e)
for i in range(len(f)-1):
    if ((len(str(f[i]))==4 and len(str(f[i+1]))!=4 or len(str(f[i+1]))==4 and len(str(f[i]))!=4)
        and ((f[i]**2+f[i+1]**2)%m5==0)):
        k+=1
        maxsum=max(maxsum,f[i]**2+f[i+1]**2)
print(k,maxsum)