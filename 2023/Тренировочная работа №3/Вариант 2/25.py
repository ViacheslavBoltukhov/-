from itertools import product
m=[]
for k in range(4):
    for i in product(range(10),repeat=k):
        m.append(''.join(str(x) for x in i))
for i in range(10):
    for elem in m:
        n='1'+str(i)+'2655'+elem+'8'
        if int(n)%4173==0:
            print(n)