maxl=0
l=0
for i in 0,1,2:
    s=open('24-197.txt').readline()[i:]
    for j in range(0,len(s)-2 ,3):
        if s[j+2]=='Y' and (s[j]=='X' or s[j]=='Z'):
            l+=1
        else:
            maxl=max(l,maxl)
            l=0
print(maxl)