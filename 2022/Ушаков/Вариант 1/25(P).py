for i in range(150000,200001,2):
    count=0
    for j in range(2,i//2+1):
        if i%j==0:
            count+=1
    if count==48:
        print(i//2)