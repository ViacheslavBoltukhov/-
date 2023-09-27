f=open('Мастер и Маргарита.txt')
count=0
c=['-',',','.']
for elem in f:
    m=elem.split()
    for s in m:
        if 'Фагот' in s:
            if s=='Фагот':
                count+=1
            elif s[5] in c:
                count+=1
                print(s)
print(count)
