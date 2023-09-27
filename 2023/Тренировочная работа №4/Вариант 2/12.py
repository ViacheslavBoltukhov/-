for i in range(100,150):
    s='0'+'12'*i+'0'
    while not ('00' in s):
        s=s.replace('02','101',1)
        s=s.replace('11','2',1)
        s=s.replace('12','21',1)
        s=s.replace('010','00',1)
    summa=0
    for e in s:
        summa+=int(e)
    if (2**summa-2)%summa==0:
        print(i)
        break
