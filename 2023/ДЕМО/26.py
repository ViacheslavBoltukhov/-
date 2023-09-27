n=list(map(int, open('26.txt').readlines()))
l=n[0]
n.pop(0)
count=1
max_count=0
max_len=0
n.sort(reverse=True)
for i in range(l-1):
    x=i
    for j in range(i+1,l):
        if n[x]-n[j]>2:
            x=j
            count+=1
    if count>max_count:
        max_count=count
        max_len=n[x]
    elif count==max_count:
        max_len=max(max_len,n[x])
    count=1
print(max_count,max_len)