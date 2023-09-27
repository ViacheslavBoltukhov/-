for i in range(70,100):
    s='0'+'12'*i+'0'
    while not ('00' in s):
        s=s.replace('02','101',1)
        s=s.replace('11','2',1)
        s=s.replace('12','21',1)
        s=s.replace('010','00',1)
    summa=0
    for e in s:
        summa+=int(e)
    flag=True
    for d in range(2,int(summa**0.5)+1):
        if summa%d==0:
            flag=False
            break
    if flag:
        print(i, summa)
        break
