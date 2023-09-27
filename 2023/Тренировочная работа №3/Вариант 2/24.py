f=open('24.txt')
m=0
for elem in f:
    s=elem
    l,ml,b=1,0,''
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            l+=1
        else:
            if l>ml:
                b=s[i-1]
                ml=l
            l=1
    if l > ml:
        b = s[i - 1]
        ml = l
    if ml>m:
        m=ml
        bm=s.count(b)
    elif ml==m and s.count(b)<bm:
        bm=s.count(b)
print(bm)