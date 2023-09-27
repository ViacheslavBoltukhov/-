for i in range(200000004,400000001,6):
    x=i
    m=0
    n=0
    while x%2==0:
        m+=1
        x//=2
    while x%3==0:
        n+=1
        x//=3
    if x==1 and m%2==0 and n%2==1:
        print(i)
        
