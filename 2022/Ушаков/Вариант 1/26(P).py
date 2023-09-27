n=list(map(int, open('26.txt').readlines()[1:]))
count=0
sum=0
for elem in n:
    if sum+1>=elem:
        sum+=elem
        count+=1
print(sum+1,count)