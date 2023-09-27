from itertools import  product
a=list(product('ГЕПАРД',repeat=5))
count=0
for elem in a:
    if elem.count('Г')==1 and elem[0]!='А' and elem[4]!='Е':
        count+=1
print(count)