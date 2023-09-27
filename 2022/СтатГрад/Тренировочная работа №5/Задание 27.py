n=list(map(int, open('27-B.txt').readlines()))
d89=0
d103=0
d107=0
count=0
for i in range(1,len(n)):
    if n[i]%89==0: d89=i
    if n[i]%103==0: d103=i
    if n[i]%107==0: d107=i
    count+=(i-min(d89,d103,d107))
print(count)