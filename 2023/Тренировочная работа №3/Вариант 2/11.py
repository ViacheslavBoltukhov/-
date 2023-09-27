from math import ceil
i=0
while 2**i<1984:
    i+=1
print(ceil(ceil(114*i/8)*32768/1024))