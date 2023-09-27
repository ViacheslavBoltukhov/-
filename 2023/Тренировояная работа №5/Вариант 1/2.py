print('x y z w 1 2')
for f1 in 0,1:
    for f2 in 0, 1:
        for x in 0, 1:
            for y in 0, 1:
                for z in 0, 1:
                    for w in 0, 1:
                        if not((x or not y)<=(w==z)) and not((x or not y)==(z<=w)) and f1==0 and f2==0:
                            print(x,y,z,w,f1,f2)
                        if not((x or not y)<=(w==z)) and ((x or not y)==(z<=w)) and f1==0 and f2==1:
                            print(x,y,z,w,f1,f2)
                        if ((x or not y)<=(w==z)) and not((x or not y)==(z<=w)) and f1==1 and f2==0:
                            print(x,y,z,w,f1,f2)