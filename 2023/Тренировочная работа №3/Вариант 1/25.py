n=1072461
while n%4173!=0:
    n+=1
for i in range(n,10**10+1,4173):
    x=str(i)
    if x[0]=='1' and x[2:6]=='7246' and x[-1]=='1':
        print(x)