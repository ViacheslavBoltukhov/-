print('x y z w F')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not((x<=(y==w)) and (y==(w<=z))):
                    if (str(x)+str(y)+str(z)+str(w)).count('1')==1:
                        print(x,y,z,w,0)
print('x y z w F')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if  ((x <= (y == w)) and (y == (w <= z))):
                    if (str(x) + str(y) + str(z) + str(w)).count('1') < 3:
                        print(x, y, z, w, 1)
