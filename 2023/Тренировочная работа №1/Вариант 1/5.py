for n in range(10000):
    x=bin(n)[2:]
    r=''
    for elem in x:
        if elem=='0':
            r+='1'
        else:
            r+='0'
    r=int(r,2)
    if n-r==999:
        print(n)
        break

