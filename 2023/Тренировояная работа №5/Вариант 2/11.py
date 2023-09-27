from math import ceil
#Код
k1=11
n1=36
i1=0
while 2**i1<n1:
    i1+=1
Ik=ceil(k1*i1/8)
#Структура
k2=30
n2=1500
i2=0
while 2**i2<n2:
    i2+=1
Is=ceil(k2*i2/8)
print(2*2**20/32768-Ik-Is)