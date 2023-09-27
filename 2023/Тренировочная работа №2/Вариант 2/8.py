count=0
b=['П','О','Л','И','Н','А']
for k1 in b:
    for k2 in b:
        for k3 in b:
            for k4 in b:
                for k5 in b:
                    for k6 in b:
                        for k7 in b:
                            for k8 in b:
                                s=k1+k2+k3+k4+k5+k6+k7+k8
                                if s.count('П')+s.count('Л')+s.count('Н')>s.count('О')+s.count('И')+s.count('А'):
                                    count+=1
print(count)