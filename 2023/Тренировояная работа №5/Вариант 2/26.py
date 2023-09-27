f=open('26.txt')
n=int(f.readline())
m=[]
for elem in f:
    tn,tp,ta=map(str, elem.split())
    m.append([int(tn), int(tp), ta])
m=sorted(m)
a=[0]*70
b=[0]*30
km=0
k=0
for elem in m:
    flag=True
    if elem[2]=='B':
        for i in range(len(b)):
            if b[i]<=elem[0]:
                km+=1
                b[i]=elem[0]+elem[1]
                flag=False
                break
    else:
        for i in range(len(a)):
            if a[i]<=elem[0]:
                a[i]=elem[0]+elem[1]
                flag=False
                break
        if flag:
            for i in range(len(b)):
                if b[i]<=elem[0]:
                    b[i]=elem[0]+elem[1]
                    flag=False
                    break
    if flag:
        k+=1
print(km,k)