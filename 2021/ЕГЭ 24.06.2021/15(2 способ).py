for a in range(1,100)[::-1]:
    if (all([(2*x+y!=48) or (x<y) or (a<x) for x in range(1,101) for y in range(1,101)])):
                print(a)
                break