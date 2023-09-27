def f(a,b):
    if b==0:
        return a
    if a>=b and b>0:
        return f(a-b,b)
    return f(b,a)
k2=(1234567888-123456795)//2
k7=(1234567888-123456795)//7//2
print(k2-k7)