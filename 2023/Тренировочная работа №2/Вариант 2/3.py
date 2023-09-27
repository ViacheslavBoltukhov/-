tor,tov=[],[]
f=open('032.csv')
for elem in f:
    s=elem.split(';')
    if s[1]=='Мясная гастрономия':
        tov.append(s[0])
f=open('031.csv').readlines()[3:]
for elem in f:
    s=elem.split(';')
    if int(s[1][:2])>6 and int(s[1][:2])<10 and s[4]=='Продажа' and s[3] in tov:
        tor.append(s)
summ=[0]*101
for elem in tor:
    summ[int(elem[2][1:])]+=int(elem[5])*int(elem[6])
print(max(summ))



