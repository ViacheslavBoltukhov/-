for a in range(1,100):
    k=True
    for x in range(1,1000):
        if not((x&73==0)<=((x&28!=0)<=(x&a!=0))):
            k=False
    if k:
        print(a)
        break
        
