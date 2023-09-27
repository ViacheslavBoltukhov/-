from math import factorial as fa
n=12
k=3
print((fa(n)//(fa(n-k)*fa(k))-(n-2+2*sum([i for i in range(n-2)])))*4**n -
      (fa(n-1)//(fa(n-1-k)*fa(k))-(n-1-2+2*sum([i for i in range(n-2-1)])))*4**(n-1))
from itertools import combinations
k0,k=0,0
for i in combinations(range(12),3):
    if i[1]-i[0]>1 and i[2]-i[1]>1:
        if i[0]!=0:
            k+=1
        else:
            k0+=1
print(k0*4**12+k*3*4**11)