m=[]
for i in range(10):
    n='1'+str(i)+'954'+'21'
    if int(n)%3023==0:
        m.append(int(n))
    for k1 in range(10):
        n = '1' + str(i) + '954' + str(k1) + '21'
        if int(n) % 3023 == 0:
            m.append(int(n))
        for k2 in range(10):
            n = '1' + str(i) + '954' + str(k1) + str(k2) + '21'
            if int(n) % 3023 == 0:
                m.append(int(n))
            for k3 in range(10):
                n = '1' + str(i) + '954' + str(k1) + str(k2) + str(k3) + '21'
                if int(n) % 3023 == 0:
                    m.append(int(n))
print(sorted(m))