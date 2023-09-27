m=['Н','А','С','Т','Я']
k=0
for i1 in range(5):
    s1=''
    s1+=m[i1]
    for i2 in range(5):
        s2=s1
        s2+=m[i2]
        for i3 in range(5):
            s3=s2
            s3+=m[i3]
            for i4 in range(5):
                s4=s3
                s4+=m[i4]
                for i5 in range(5):
                    s5=s4
                    s5+=m[i5]
                    for i6 in range(5):
                        s6=s5
                        s6+=m[i6]
                        if s6.count('А')<=1 and s6.count('Я')<=1:
                            k+=1
print(k)
