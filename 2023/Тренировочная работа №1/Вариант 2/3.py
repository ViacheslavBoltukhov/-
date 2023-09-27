f=open('32.txt')
o,r,p=[],[],[]
for elem in f:
    s=elem.split('\t')
    if s[1]=='Бакалея':
        o.append(s[0])
f=open('33.txt')
for elem in f:
    s=elem.split('\t')
    if s[1]=='Первомайский\n':
        r.append(s[0])
f=open('31.txt').readlines()[3:]
for elem in f:
    s=elem.split('\t')
    if int(s[1][:2])>13 and int(s[1][:2])<21 and s[4]=='Продажа':
        p.append(elem)
sum=0
for elem in p:
    i1 = elem.split('\t')
    for i2 in o:
        for i3 in r:
            if (i2==i1[3]) and (i3==i1[2]):
                sum=sum+int(i1[5])*int(i1[6])
print(sum)