for n in range(1294578,10**9+1,3127):
    x=str(n)
    if x[:2]=='12' and x[-2]=='1' and x[-5:-3]=='93':
        print(x)
print([if (str(x[:2])=='12' and str(x[-2])=='1' and str(x[-5:-3])=='93') for x in range(1294578,10**9+1,3127)])