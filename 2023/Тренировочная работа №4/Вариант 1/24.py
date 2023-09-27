f=open('24.txt')
ans=[0]*100
for e in f:
    a=[0]*100
    for i in range(len(e)-1):
        if e[i]=='A':
            a[ord(e[i+1])]+=1
    m=max(a)
    for i in range(len(a)):
        if a[i]==m:
            ans[i]+=1
print(max(ans))