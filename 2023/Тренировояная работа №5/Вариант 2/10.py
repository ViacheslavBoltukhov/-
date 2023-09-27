f=open('Мастер и Маргарита.txt').readlines()
k=0
for elem in f:
    if 'Глава' in elem:
        k=elem
    if 'Фагот' in elem:
        break
print(k[-3:])