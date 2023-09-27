def newnum(n):
    n = bin(n)[2:]
    if int(n)%2==0:
        return int('1' + n + '0')
    else:
        return int('11' + n + '11')
for n in range(100):
    if newnum(n) > int(bin(52)[2:]):
        print(n)
        break
