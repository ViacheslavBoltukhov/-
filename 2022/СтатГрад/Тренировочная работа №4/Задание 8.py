from itertools import product
count=0
for elem in product('НАСТЯ', repeat=7):
    s=''.join(elem)
    if s.count('Н')==2 and s.count('А')>0:
        count+=1
print(count)