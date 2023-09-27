from itertools import *
a=list(product('ЕЛМРУ',repeat=4))
print(a)
for i in range(len(a)):
    if a[i][0]=='Л':
        print(i+1)
        break