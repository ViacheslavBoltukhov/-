numbs=list(map(int, open('27-B.txt').readlines()))
n=numbs[0]
numbs.pop(0)
count=0
ost=[0]*999
massiv_summ=[0]
summa=0
for i in range(100):
    summa+=numbs[i]
    massiv_summ.append(summa)
for i in range(100,n):
    ost[massiv_summ[0]%999]+=1
    summa+=numbs[i]
    count+=ost[summa%999]
    massiv_summ.pop(0)
    massiv_summ.append(summa)
print(count)