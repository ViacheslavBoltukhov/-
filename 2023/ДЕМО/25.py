'''1 Вариант'''
for k1 in range(10):
    n1='1'+str(k1)+'2139'
    if int(n1+'4')%2023==0:
        print(int(n1+'4'),int(n1+'4')//2023)
    for k2 in range(10):
        n2=n1+str(k2)
        if int(n2+'4')%2023==0:
            print(int(n2+'4'),int(n2+'4')//2023)
        for k3 in range(10):
            n3=n2+str(k3)
            if int(n3+'4')%2023==0:
                print(int(n3+'4'),int(n3+'4')//2023)
            for k4 in range(10):
                n4=n3+str(k4)
                if int(n4+'4')%2023==0:
                    print(int(n4+'4'),int(n4+'4')//2023)
'''2 Вариант'''
for k1 in range(10):
    n1='1'+str(k1)+'2139'
    if int(n1+'4')%2023==0:
        print(int(n1+'4'),int(n1+'4')//2023)
    for k2 in range(10):
        n2=n1+str(k2)+'4'
        if int(n2)%2023==0:
            print(int(n2),int(n2)//2023)
    for k2 in range(10):
        for k3 in range(10):
           n2=n1+str(k2)+str(k3)+'4'
           if int(n2) % 2023 == 0:
               print(int(n2), int(n2) // 2023)
    for k2 in range(10):
        for k3 in range(10):
            for k4 in range(10):
                n2=n1+str(k2)+str(k3)+ str(k4)+'4'
                if int(n2) % 2023 == 0:
                    print(int(n2), int(n2) // 2023)