for i in range(200):
    n = bin(i)[2:]
    sumn = sum(map(int, n))
    r = str(n)+str(int(sumn)%2)
    n = r
    sumn = sum(map(int, n))
    r = str(n)+str(int(sumn)%2)
    if int(r)>110001100:
        print(i,r)
        break
    
