n=list(map(int, open('17.txt').readlines()))
summa=0
count=0
for elem in n:
    if elem%2==1:
        summa+=elem
        count+=1
mid=summa/count
summax=0
count=0
for i in range(len(n)-2):
    d={n[i]%3,n[i+1]%3,n[i+2]%3}
    k=0
    if n[i]<mid: k+=1
    if n[i+1]<mid: k+=1
    if n[i+2]<mid: k+=1
    if len(d)==3 and k==1:
        count+=1
        summax=max(summax,n[i]+n[i+1]+n[i+2])
print(count,summax)
