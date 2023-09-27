n='0123456789'
for k1 in n:
    s='1'+k1+'6961'+'5'
    if int(s)%3013==0:
        print(s)
    for k2 in n:
        s = '1' + k1 + '6961' + k2 + '5'
        if int(s) % 3013 == 0:
            print(s)
        for k3 in n:
            s = '1' + k1 + '6961' + k2 + k3 + '5'
            if int(s) % 3013 == 0:
                print(s)
            for k4 in n:
                s = '1' + k1 + '6961' + k2 + k3 + k4 + '5'
                if int(s) % 3013 == 0:
                    print(s)