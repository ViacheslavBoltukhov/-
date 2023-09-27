f=open('Мастер и Маргарита.txt').readlines()
for string in f:
    s=string.split(' ')
    for elem in s:
        if 'емец' in elem:
            print(elem)
