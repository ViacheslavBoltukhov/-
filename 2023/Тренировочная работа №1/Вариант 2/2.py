print('x y z w F')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not((w<=(y==z)) and (y==(z<=x))) and (x+y+z+w==1):
                    print(x,y,z,w,0)
print('x y z w F')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (w<=(y==z)) and (y==(z<=x)) and (x+y+z+w<4):
                    print(x,y,z,w,1)