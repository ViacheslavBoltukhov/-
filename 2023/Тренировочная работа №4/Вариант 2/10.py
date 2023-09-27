f=list(map(str, open('Мастер и Маргарита.txt').readlines()))
for elem in f:
    s=list(map(str, elem.split()))
    for i in range(1,len(s)-1):
        if 'осен' in s[i] or 'Осен' in s[i]:
            print(s[i])