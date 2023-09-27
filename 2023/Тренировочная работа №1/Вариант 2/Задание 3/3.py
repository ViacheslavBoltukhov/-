t1,t2,t3=[],[],[]
f=open('31.csv').readlines()[3:]
for elem in f:
    s=elem.split(';')
    if int(s[1][:2])>13 and int(s[1][:2])<21 and s[4]=='Продажа':
        t1.append(elem)
f=open('32.csv').readlines()[2:]
for elem in f:
    s=elem.split(';')
    if s[1]=='Бакалея':
        t2.append(s[0])
f=open('33.csv').readlines()[1:]
for elem in f:
    s=elem.split(';')
    if s[1].strip()=='Первомайский':
        t3.append(s[0])
sum=0
for elem in t1:
    i1=elem.split(';')
    for i2 in t2:
        for i3 in t3:
            if (i2==i1[3]) and (i3==i1[2]):
                sum=sum+int(i1[5])*int(i1[6])
print(sum)