from itertools import product
count=0
for elem in product('СВЕТЛАН',repeat=8):
    s=''.join(elem)
    if (s.count('А')==2 and s.count('АА')==0 and
        s.count('С') == s.count('В') == s.count('Т') == s.count('Л') == s.count('Н') == s.count('Е') == 1):
        count+=1
print(count)