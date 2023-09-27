from itertools import product
for i in range(1,15):
    for elem in product('12',repeat=i):
        print(''.join(elem))