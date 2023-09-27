from itertools import product
number=1
for elem in product('АВОРТ',repeat=4):
    if ''.join(elem)=='ВАТА':
        print(number)
        break
    number+=1