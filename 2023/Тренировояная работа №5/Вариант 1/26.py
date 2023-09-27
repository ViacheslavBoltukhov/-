f=open('26.txt')
n=int(f.readline())
m=[]
for elem in f:
    tn,tp,ta=map(str, elem.split())
    m.append([int(tn),int(tp),ta])
m=sorted(m)
a=[0]*80
b=[0]*20
kl=0
k=0
for elem in m:
    if elem[2]=='B':
        flag=True
        for i in range(len(b)):
            if b[i]<=elem[0]:
                b[i]=elem[0]+elem[1]
                flag=False
                break
        if flag:
            k+=1
    else:
        flag=True
        for i in range(len(a)):
            if a[i]<=elem[0]:
                a[i]=elem[0]+elem[1]
                kl+=1
                flag=False
                break
        if flag:
            for i in range(len(b)):
                if b[i]<=elem[0]:
                    b[i]=elem[0]+elem[1]
                    kl+=1
                    flag=False
                    break
        if flag:
            k+=1
print(kl,k)