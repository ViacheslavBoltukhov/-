tor,tov,mag=[],[],[]
f=open('031.csv')
n=0
for elem in f:
    s=elem.split(';')
    if (s[1]=='28.06.2021' or s[1]=='29.06.2021' or s[1]=='30.06.2021') and s[4]=='Поставка':
        tor.append(s)
        n=max(n,int(s[2][1:]))
m=[0]*(n+1)
f=open('032.csv')
for elem in f:
    s=elem.split(';')
    if s[1]=='Мясная гастрономия':
        tov.append(s)
for elem in tor:
    for k in tov:
        if elem[3]==k[0]:
            m[int(elem[2][1:])]+=int(elem[5])*float(k[4].replace(',','.'))
f=open('033.csv')
r=[]
for elem in f:
    s=elem.split(';')
    mag.append(s)
    if s[1] not in r:
        r.append(s[1])
r=r[1:]
sumr=[0]*len(r)
for elem in mag:
    for i in range(len(r)):
        if elem[1]==r[i]:
            sumr[i]+=m[int(elem[0][1:])]
for i in range(len(r)):
    print(r[i][:-1],'-',sumr[i])
print(min(sumr))
