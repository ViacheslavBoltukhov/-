for x in range(2,1000):
    s=str(x)
    sum1=0
    sum2=0
    for i in range(len(s)):
        if int(s[i])%2==0:
            sum1+=int(s[i])
        if i%2==1:
            sum2+=int(s[i])
    if abs(sum2-sum1)==13:
        print(x)
        break