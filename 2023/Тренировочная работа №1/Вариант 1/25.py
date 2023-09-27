ww=[]
for i in range(10):
    n='1'+str(i)+'493'+'41'
    if int(n)%2023==0:
        ww.append(int(n))
    for p in range(10):
        n = '1' + str(i) + '493' + str(p) + '41'
        if int(n) % 2023 == 0:
            ww.append(int(n))
        for w in range(10):
            n = '1' + str(i) + '493'+ str(p) + str(w) + '41'
            if int(n) % 2023 == 0:
                ww.append(int(n))
            for t in range(10):
                n = '1' + str(i) + '493'+ str(p) + str(w)+ str(t) + '41'
                if int(n) % 2023 == 0:
                    ww.append(int(n))
print(sorted(ww))
