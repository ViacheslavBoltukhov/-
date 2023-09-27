print('x y z w F')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((z==(not x))<=((w<=(not y)) and (y<=x))) and (x+y+z+w==3):
                    print(x,y,z,w,1)
print('x y z w F')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not((z==(not x))<=((w<=(not y)) and (y<=x))):
                    print(x,y,z,w,0)