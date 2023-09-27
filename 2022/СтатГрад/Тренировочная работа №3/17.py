numbs=list(map(int, open('17.txt').readlines()))
sum_chet=0
count_chet=0
for numb in numbs:
    if numb%2==0:
        sum_chet+=numb
        count_chet+=1
mid=sum_chet/count_chet
count_two=0
max_sum_two=0
for i in range(len(numbs)-1):
    if (numbs[i]%3==0 and numbs[i+1]<mid) or (numbs[i+1]%3==0 and numbs[i]<mid):
        count_two+=1
        max_sum_two=max(max_sum_two,numbs[i]+numbs[i+1])
print(count_two,max_sum_two)