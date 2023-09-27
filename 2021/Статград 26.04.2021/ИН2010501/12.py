for i1 in range(1,30):
    s='0'
    s1=s+i1*'1'
    for i2 in range(1,30):
        s2=s1
        s2=s1+i2*'2'
        for i3 in range(1,30):
            s3=s2
            s3=s2+'3'*i3
            s=s3+'0'
            while '00' not in s:
                s=s.replace('01','210',1)
                s=s.replace('02','320',1)
                s=s.replace('03','3012',1)
            if s.count('1')==23 and s.count('2')==48 and s.count('3')==41:
                print('1 -',i1)
                print('2 -',i2)
                print('3 -',i3)
                
