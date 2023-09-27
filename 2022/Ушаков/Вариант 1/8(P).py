from itertools import product
count=0
for elem in product('СТЕПАН',repeat=4):
    s=''.join(elem)
    if s.count('Т')==1:
        count+=1
print(count)