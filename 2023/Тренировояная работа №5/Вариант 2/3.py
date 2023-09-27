tor,tov,mag=[],[],[]
f=open('031.csv').readlines()[3:]
for e in f:
    elem=e.rstrip().split(';')
    if int(elem[1][:2])>=21 and int(elem[1][:2])<=25 and elem[4]=='Поставка':
        tor.append(elem)
        #print(elem)
f=open('032.csv').readlines()[2:]
for e in f:
    elem=e.rstrip().split(';')
    if elem[-1]=='Молокозавод №2':
        tov.append(elem)
        #print(elem)
f=open('033.csv').readlines()[1:]
for e in f:
    elem=e.rstrip().split(';')
    if elem[1]=='Заречный':
        mag.append(elem)
        #print(elem)
s=0
for e_tor in tor:
    for e_tov in tov:
        if e_tor[3]==e_tov[0]:
            for e_mag in mag:
                if e_tor[2]==e_mag[0]:
                    s+=int(e_tor[-1])*int(e_tor[-2])
print(s)

