f=open('24.txt')
m=0
for string in f:
    s=string
    l,ml,b=1,0,''
    for  i in range(1,len(s)):
        if s[i-1]==s[i]:
            l+=1
        else:
            if l>ml:
                b=s[i-1]
                ml=l
            l=1
    if ml>m:
        m=ml
        bm=s.count(b)
    elif ml==m and s.count(b)>bm:
        n=ml
        bm=s.count(b)
print(bm)


