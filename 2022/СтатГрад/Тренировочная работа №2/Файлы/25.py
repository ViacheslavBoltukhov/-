count=0
x=10_000_042
while count!=5:
    x+=1
    countd=0
    a=[]
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            countd+=2
            a.append(i)
            a.append(x//i)
    a=sorted(a)
    if len(a)>1:
        if 0 < a[-1] + a[-2] < 10000:
            print(x,a[-1],a[-2],a[-1]+a[-2],a)
            count+=1

