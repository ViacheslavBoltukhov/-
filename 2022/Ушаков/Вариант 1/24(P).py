s=open('24.txt').readline()
l=1
maxl=0
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        l+=1
    else:
        maxl=max(l,maxl)
        l=1
print(max(l,maxl))
