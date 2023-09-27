point=list(sorted(list(map(int, s.split())) for s in open('26.txt').readlines()[1:]))
point.append([0,0])
max_count_point=0
count_point=1
min_n=0
n_row=0
for i in range(len(point)-1):
    if point[i+1][1]!=point[i][1] and point[i+1][1]-point[i][1]==1 and point[i+1][0]==point[i][0]:
        count_point+=1
    elif point[i+1][1]-point[i][1]>1 or point[i+1][0]!=point[i][0]:
        if count_point>max_count_point:
            max_count_point=count_point
            n_row=point[i][0]
            min_n=min(point[i][1]-count_point,10000-point[i][1],point[i][0]-1,10000-point[i][0])
        elif count_point==max_count_point:
            if min(point[i][1]-count_point,10000-point[i][1],point[i][0]-1,10000-point[i][0])<min_n:
                min_n=min(point[i][1]-count_point,10000-point[i][1],point[i][0]-1,10000-point[i][0])
                n_row=point[i][0]
        count_point=1
print(n_row,min_n)