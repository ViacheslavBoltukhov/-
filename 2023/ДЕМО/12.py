for i in range(117,200,4):
    flag=True
    for j in range(2,i//2+1):
        if i%j==0:
            flag=False
            break
    if flag:
        print((i-117)//4)
        break
