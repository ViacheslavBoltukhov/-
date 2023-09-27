s=open('24.txt').readline()
m=s.replace('A','1').replace('O','1').split('1')
count=0
maxcount=0
for i in range(len(m)):
    if len(m[i])==2:
        count+=1
    else:
        if i-count-1>=0:
            if len(m[i-count-1])>=2:
                count+=1
        maxcount=max(count,maxcount)
        count=0
print(maxcount)