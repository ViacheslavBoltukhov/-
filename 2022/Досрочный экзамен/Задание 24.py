s=open('24.txt').readline()
a=s.replace('AC','1').replace('AB','1')
count=0
maxcount=0
for elem in a:
    if elem=='1':
        count+=1
    else:
        maxcount=max(count,maxcount)
        count=0
print(maxcount)