f=open('24.txt').readline()
count=0
maxcount=0
k=0
flag=True
for elem in f:
    if elem=='A' or elem=='O':
        k+=1
    else:
        if k>2 and flag:
            count+=1
            flag=False
        elif k==2:
            count+=1
        else:
            maxcount=max(count,maxcount)
            count=0
            flag=True
        k=0
print(max(count,maxcount))
