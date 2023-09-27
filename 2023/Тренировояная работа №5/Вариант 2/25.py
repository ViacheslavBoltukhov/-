n=1027110
for x in range(n,10**10+1,4891):
    s=str(x)
    if s[0]=='1' and s[2:6]=='2711' and s[-1]=='0':
        print(s)