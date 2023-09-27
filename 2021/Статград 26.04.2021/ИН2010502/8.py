for i in range(50):
    s = '0'
    s1 = s + '1'*i
    for j in range(50):
        s2 = s1 + j*'2'
        for k in range(50):
            s3 = s2 + '3'*k+'0'
            s = s3
            while '00' not in s:
                s = s.replace('01','210',1)
                s = s.replace('02','320',1)
                s = s.replace('03','3012',1)
            if s.count('1')==26 and s.count('2')== 54 and s.count('3')==48:
                print(i+j+k+2)
                
