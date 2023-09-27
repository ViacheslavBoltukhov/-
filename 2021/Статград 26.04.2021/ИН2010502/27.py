pairs = [list(map(int, pair.split())) for pair in open('27-B.txt').read().splitlines()]
new_pairs=list(filter(lambda x: x[1]%2!=0,pairs))
sum_max=sum(max(pair) for pair in new_pairs)
sum_min=sum(min(pair) for pair in new_pairs)
sum_elem=[]
for i in range(len(new_pairs)):
    sum_elem.append(new_pairs[i][0]+new_pairs[i][1])
sum_elem.sort()
new_sum_max=0
new_sum_min=0
ans_sum=0
if sum_max%2==0 and sum_min%2!=0:
    print(sum_max+sum_min)
else:
    for pair in new_pairs:
        new_sum_max=sum_max-max(pair)
        new_sum_min=sum_min-min(pair)
        if new_sum_max%2==0 and new_sum_min%2!=0 and (new_sum_max+new_sum_min)>ans_sum:
            ans_sum=new_sum_max+new_sum_min
    if ans_sum>sum_max+sum_min-(sum_elem[0]+sum_elem[1]):
        print(ans_sum)
    else:
        print(sum_max+sum_min-(sum_elem[0]+sum_elem[1]))
