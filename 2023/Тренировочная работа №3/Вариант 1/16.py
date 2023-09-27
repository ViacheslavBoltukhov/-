def f(a,b):
    if a==0 and b==0:
        return 0
    if a>b:
        return f(a-1,b)+b
    if a<=b and b>0:
        return f(a,b-1)+a
count=0
m=[]
if int(1048576**0.5)==1048576**0.5:
    count+=1
    m.append(int(1048576**0.5))
for i in range(1,int(1048576**0.5)):
    if 1048576%i==0:
        count+=2
        m.append(i)
        m.append(1048576//i)
print(count)
print(sorted(m))