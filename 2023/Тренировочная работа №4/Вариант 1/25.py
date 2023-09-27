for i in range(1039485,10**10+1,3013):
    n=str(i)
    if n[0]=='1' and n[2:6]=='3948' and n[-1]=='5':
        print(n)