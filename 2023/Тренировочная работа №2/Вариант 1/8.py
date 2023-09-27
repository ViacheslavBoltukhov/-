from itertools import product
k=0
for elem in product('ВЕРОНИКА',repeat=6):
    s=''.join(elem)
    if s.count('Е')+s.count('О')+s.count('И')+s.count('А')>s.count('В')+s.count('Р')+s.count('Н')+s.count('К'):
        k+=1
print(k)