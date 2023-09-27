numbs=list(map(int, open('17.txt').readlines()))
count=0
max_sum=0
for i in range(len(numbs)-1):
    if (numbs[i]%3==0 or numbs[i+1]%3==0):
        if (numbs[i]+numbs[i+1])%5==0:
            max_sum=max(max_sum,numbs[i]+numbs[i+1])
            count+=1
print(count,max_sum)
