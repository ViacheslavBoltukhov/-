p = range(17,55)
q = range(37, 84)
k = 0
for i in range(2,100):
    a = range(1, i)
    for x in range(1,100):
        if (x in p) <= (((x in q) and not(x in a)) <= (not(x in p))):
            k+=1
    if k==i-1:
        print(a)
