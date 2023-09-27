times=list(list(map(int, s.split())) for s in map(str, open('26.txt').read().splitlines()))
n=times[0][0]
times.pop(0)
time=[0]*604801
time_start=1633305600
time_end=time_start+7*24*3600
count=0
for elem in times:
    start=elem[0]
    end=elem[1]
    if start<time_start and (end>time_start or end==0):
        count+=1
    if time_start<=start<=time_end:
        time[start-time_start]+=1
    if time_start<=end<=time_end:
        time[end-time_start]-=1
max_time=0
max_count=0
for elem in time:
    count+=elem
    if count>max_count:
        max_count,max_time=count,0
    if count==max_count:
        max_time+=1
print(max_count,max_time)




