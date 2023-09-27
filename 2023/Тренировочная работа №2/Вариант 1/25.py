m=[]
for k1 in range(10):
    for k2 in range(10):
        n='12'+'63'+str(k1)+'5'+str(k2)
        if int(n)%3123==0:
            m.append(int(n))
        for x1 in range(10):
            n='12'+str(x1)+'63'+str(k1)+'5'+str(k2)
            if int(n) % 3123 == 0:
                m.append(int(n))
            for x2 in range(10):
                n = '12' + str(x1) + str(x2) + '63' + str(k1) + '5' + str(k2)
                if int(n) % 3123 == 0:
                    m.append(int(n))
print(sorted(m))
m=[]
from itertools import product
for k1 in range(10):
    for k2 in range(10):
        for x in range(3):
            for elem in product('0123456789',repeat=x):
                n = '12' + ''.join(elem) + '63' + str(k1) + '5' + str(k2)
                if int(n) % 3123 == 0:
                    m.append(int(n))
print(sorted(m))