point=list(sorted(list(map(int, s.split())) for s in open('26.txt').readlines()[1:]))
point.append([0,0])
max_count_point=0
count_point=0
min_number=0
for i in range(len(point)-1):
    if point[i][1]%2==0 and point[i][1]!=point[i+1][1]:
        count_point+=1
    if point[i][0]!=point[i+1][0]:
        if count_point>max_count_point:
            max_count_point=count_point
            min_number=point[i][0]
        count_point=0
print(max_count_point,min_number)