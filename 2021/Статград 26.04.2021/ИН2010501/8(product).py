from itertools import*
a=product('НАСТЯ', repeat=6)
k=0
for string in a:
    if string.count('А')<=1 and string.count('Я')<=1:
        k+=1
print(k)
