print('x y z w F')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (x==(not y))<=((z<=(not w)) and (w<=y)) ) and (x+y+z+w==3):
                    print(x,y,z,w,1)
print('x y z w F')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not(( (x==(not y))<=((z<=(not w)) and (w<=y)) )):
                    print(x,y,z,w,0)