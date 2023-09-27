def f(n):
    if n>1000000:
        return n
    return n+f(2*n)
def g(n):
    return f(n)/n
k=0
x=g(2000)
for i in range(1,1000001):
    if g(i)==x:
        k+=1
print(k)