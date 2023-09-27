count=0
for i in range(8**4,8**5):
    x=oct(i)[2:]
    if x.count('6')==1:
        n=x.find('6')
        if n==0 and int(x[1])%2==0:
            count+=1
        elif n==4 and int(x[3])%2==0:
            count+=1
        elif int(x[n-1])%2==0 and int(x[n+1])%2==0:
            count+=1
print(count)
