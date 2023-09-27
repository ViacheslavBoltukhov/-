def f(a,b):
    if a==b==0:
        return 0
    if a>b:
        return f(a-1,b)+b
    elif a<=b and b>0:
        return f(a,b-1)+a
count=0
m=[]
if int(2097152**0.5)==2097152**0.5:
    count+=1
    m.append(int(2097152**0.5))
for i in range(1,int(2097152**0.5)):
    if 2097152%i==0:
        count+=2
        m.append(i)
        m.append(2097152//i)
print(count)
print(sorted(m))