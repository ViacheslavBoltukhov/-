point=list(list(map(int, string.split())) for string in map(str, open('26.txt').read().splitlines()))
n=point[0]
point.pop(0)
point=sorted(point)
maxpoint=0
minrow=0
countpoint=1
for i in range(1,len(point)):
    if point[i]==point[i-1]:
        continue
    if point[i][0]==point[i-1][0] and point[i][1]-point[i-1][1]==1:
        countpoint+=1
        if countpoint>maxpoint:
            maxpoint=countpoint
            minrow=point[i][0]
    else:
        countpoint=1
print(maxpoint,minrow)
