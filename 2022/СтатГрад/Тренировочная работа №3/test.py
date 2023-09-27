numbs=list(map(int,open('27-B.txt').readlines()))
n=numbs[0]
numbs.pop(0)
count=0
n=[0]*999
summa=0
n[0]=1
for numb in numbs:
    summa+=numb
    count+=n[summa%999]
    n[summa % 999]+=1
print(count)

