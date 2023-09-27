print('x y z w 1 2')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not( (w or not y)<=(z==x)) and not((w or not y)==(x<=z)):
                    print(x,y,z,w,0,0)
                if not( (w or not y)<=(z==x)) and ((w or not y)==(x<=z)):
                    print(x,y,z,w,0,1)
                if ( (w or not y)<=(z==x)) and not((w or not y)==(x<=z)):
                    print(x,y,z,w,1,0)