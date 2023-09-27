from itertools import product
k=0
g='ИОА'
s='МТРФН'
for elem in product('МИТРОФАН',repeat=6):
    a=list(elem)
    if len(set(a))==6:
        ks=0
        kg=0
        for e in a:
            if e in s:
                ks+=1
            else:
                kg+=1
        if ks>kg:
            flag=True
            for i in range(len(a)-1):
                if a[i] in g and a[i+1] in g:
                    flag=False
                    break
            if flag:
                k+=1
print(k)