from math import *
#ID
n=26
i=0
while 2**i<n:
    i+=1
id=ceil(i*7/8)
#Серуктура
n=1789
i=0
while 2**i<n:
    i+=1
st=ceil(i*70/8)
print(2*2**20/16384-(id+st))