tor=[]
f=open('031.csv').readlines()[3:]
n=0
for elem in f:
    s=elem.split(';')
    if int((s[1][:2]))>=14 and int((s[1][:2]))<=18 and s[4]=='Продажа':
        tor.append(s)
        n=max(n,int(s[2][1:]))
m=[0]*(n+1)
f=open('032.csv').readlines()[2:]
tov=[]
for elem in f:
    s=elem.split(';')
    if s[1]=='Бакалея':
        tov.append(s)
for elem in tor:
    for k in tov:
        if elem[3]==k[0]:
            m[int(elem[2][1:])]+=int(elem[5])*int(elem[6])
mag=[]
f=open('033.csv').readlines()[1:]
r=[]
for elem in f:
    s=elem.split(';')
    mag.append(s)
    if s[1] not in r:
        r.append(s[1])
sumr=[0]*len(r)
for elem in mag:
    for i in range(len(r)):
        if elem[1]==r[i]:
            sumr[i]+=m[int(elem[0][1:])]
for i in range(len(r)):
    print(r[i][:-1],'-',sumr[i])
print(max(sumr))