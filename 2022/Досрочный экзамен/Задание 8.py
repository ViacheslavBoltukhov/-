from itertools import product
k=0
for elem in product('АПРСУ',repeat=5):
    k+=1
    s=''.join(elem)
    if s[0]=='У' and s.count('АА')==0:
        print(k)
        break