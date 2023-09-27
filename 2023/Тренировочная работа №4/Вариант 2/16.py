def f(a,b):
    if b==0:
        return a
    if a>=b and b>0:
        return f(a-b,b)
    return f(b,a)
n1=123456798
k=0
while n1%15!=0:
    if n1%3!=0 and n1%5!=0:
        k+=1
    n1+=1
n2=1234567885
while n2%15!=0:
    if n2%3!=0 and n2%5!=0:
        k+=1
    n2-=1
print((n2-n1)//15*8+k)