numbs=list(map(int, open('27-B.txt').readlines()))
n=numbs[0]
numbs.pop(0)
count=0
ost=[0]*999
ost[0]=1
summa=0
for numb in numbs:
    summa+=numb
    count+=ost[summa%999]
    ost[summa%999]+=1
print(count)