k=0
count=0
while count<5:
    k+=1
    mk=950_000_000+k
    d2=0
    while mk%2==0:
        d2+=1
        mk//=2
    if d2%2==1:
        flag=True
        while mk!=1:
            d=0
            flag_d=True
            for i in range(3,int(mk**0.5)+1,2):
                if mk%i==0:
                    flag_d=False
                    while mk%i==0:
                        d+=1
                        mk//=i
                    break
            if d%2==1:
                flag=False
                break
            if flag_d:
                flag=False
                break
        if flag:
            count+=1
            print(k)
