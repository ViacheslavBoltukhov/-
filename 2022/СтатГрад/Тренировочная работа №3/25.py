n=460_000_000
count=0
while count!=5:
    n+=1
    countd=0
    a=[]
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            countd+=2
            a.append(d)
            a.append(n//d)
    a=sorted(a)
    if countd>4:
        print(a[-5])
        count+=1
