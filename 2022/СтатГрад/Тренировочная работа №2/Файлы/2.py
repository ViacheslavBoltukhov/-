print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not(((x<=y)and(z or w))<=((x==w)or(y and not z))):
                    print(x,y,z,w)