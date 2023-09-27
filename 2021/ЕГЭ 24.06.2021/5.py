def too(x):
    s=''
    while x!=0:
        s+=str(x%2)
        x//=2
    return s[::-1]
a=[]
for i in range(1,1000):
    n=''
    if i%2==0:
        n='1'+ too(i)+'0'
    else:
        n='11'+too(i)+'11'
    if int(n,2)>52:
        a.append(int(n,2))
print(min(a))
