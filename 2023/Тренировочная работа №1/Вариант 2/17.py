f=list(map(int, open('17.txt').readlines()))
min6=10001
for elem in f:
    if str(elem)[-1]=='6' and elem<min6:
        min6=elem
min6=min6**2
count=0
maxsum=0
for i in range(len(f)-1):
    if str(f[i])[-1]=='6' and str(f[i+1])[-1]!='6' or str(f[i])[-1]!='6' and str(f[i+1])[-1]=='6':
        if f[i]**2+f[i+1]**2<min6:
            count+=1
            maxsum=max(maxsum,f[i]**2+f[i+1]**2)
print(count,maxsum)