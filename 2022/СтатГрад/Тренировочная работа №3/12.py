s0='0'
for i in range(20):
    s1=s0
    s1+='1'*i
    for j in range(20):
        s2=s1
        s2+='2'*j
        for k in range(20):
            s3=s2
            s=s3+'3'*k+'0'
            l=len(s)
            while '00' not in s:
                s=s.replace('01','210',1)
                s=s.replace('02','3101',1)
                s=s.replace('03','2012',1)
            if s.count('1')==70 and s.count('2')==56 and s.count('3')==23:
                print(l)

