for a in range(1,100)[::-1]:
    k=0
    for x in range(1,51):
        for y in range(1,51):
            if 2*x+y!=70 or x<y or a<x:
                k+=1
    if k==2500:
        print(a)
        break