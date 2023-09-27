f=open('24.txt')
ans=[0]*26
for e in f:
    e=e.rstrip()
    a=[0]*26
    for i in range(len(e)-1):
        if e[i]=='T':
            a[ord(e[i+1])-65]+=1
    m=max(a)
    for i in range(len(a)):
        if a[i]==m:
            ans[i]+=1
print(max(ans))
