file=open('27_B.txt')
n=int(file.readline())
i,j,s,max_s,min_count=0,0,0,0,n
for elem in range(n):
    x=int(file.readline())
    if x%43==0:
        s+=x
        j+=1
    else:
        if s>max_s:
            max_s=s
            min_count=j-i
        if s==max_s:
            min_count=min(min_count,j-i)
        s=0
        i=j
print(min_count)