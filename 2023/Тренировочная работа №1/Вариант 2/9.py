f=open('09.csv').readlines()
count=0
for elem in f:
    s=list(map(int, elem.split(';')))
    if len(set(s))==4:
        sump=0
        sumnp=0
        for i in range(6):
            if s.count(s[i])==2:
                sump+=s[i]
            else:
                sumnp+=s[i]
        sump//=2
        if sump>sumnp:
            count+=1
print(count)
