min4=10**9
for i in range(16,21,2):
    m=set()
    from itertools import product
    for elem in product('12',repeat=i):
        s=''.join(elem)
        if s.count('1')==s.count('2'):
            m.add(s)
    for elem in m:
        s='0'+elem+'0'
        t=s
        while not('00' in s):
            if '011' in s:
                s=s.replace('011','101',1)
            else:
                s=s.replace('01','40',1)
                s=s.replace('02','20',1)
                s=s.replace('0222','1401',1)
        if s.count('1')==6 and s.count('2')==9:
            min4=min(min4,s.count('4'))
print(min4)