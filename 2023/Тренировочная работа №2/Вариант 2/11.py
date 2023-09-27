N=980
k=310
i=0
while 2**i<N:
    i+=1
from math import ceil
I=ceil(k*i/8)
print(ceil(I*16384/1024))