n=list(map(int, open('17.txt').readlines()))
m3=10**10
for elem in n:
    if len(str(elem))==3 and elem%10==3:
        m3=min(m3,elem)
def f(a,b):
    return len(str(a))==4 and len(str(b))!=4 or len(str(a))!=4 and len(str(b))==4
k=0
maxsum=0
for i in range(len(n)-1):
    if f(n[i],n[i+1]) and (n[i]**2+n[i+1]**2)%m3==0:
        k+=1
        maxsum=max(maxsum,n[i]**2+n[i+1]**2)
print(k,maxsum)