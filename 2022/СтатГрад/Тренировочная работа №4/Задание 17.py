n=list(map(int, open('17.txt').readlines()))
minn=10001
for elem in n:
    if elem%2==1 and elem<minn:
        minn=elem
maxmodul=-1
count=0
for i in range(len(n)-1):
    k=0
    if n[i]%3==0: k+=1
    if n[i+1]%3==0: k+=1
    if k==1 and abs(n[i]-n[i+1])<minn:
        count+=1
        maxmodul=max(maxmodul,abs(n[i]-n[i+1]))
print(count,maxmodul)