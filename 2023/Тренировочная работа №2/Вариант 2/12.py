m=[]
from itertools import product
for elem in product('12',repeat=20):
    s=''.join(elem)
    if s.count('1')==s.count('2'):
        m.append(s)
k4=0
for elem in m:
    s='0'+elem+'0'
    while not ('00' in s):
        s=s.replace('012','30',1)
        if '011' in s:
            s = s.replace('011', '20', 1)
            s = s.replace('022', '40', 1)
        else:
            s = s.replace('01', '10', 1)
            s = s.replace('02', '101', 1)
    if s.count('1')==6 and s.count('2')==5:
        k4=max(k4,s.count('4'))
print(k4)


