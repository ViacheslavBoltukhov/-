xmin=999999
count=0
for x in range(345678,456790):
    if not(x%(sum(map(int, str(x))))):
        count+=1
        xmin=min(x,xmin)
print(count,xmin)
        
