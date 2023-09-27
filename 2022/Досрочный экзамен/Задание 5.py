for i in range(1,1000):
    if i%2==0:
        n=int(bin(i)[2:]+'10',2)
    else:
        n = int('1' + bin(i)[2:] + '01', 2)
    if n>516:
        print(i)
        break

