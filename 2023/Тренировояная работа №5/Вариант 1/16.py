def f(n):
    if n>1000000:
        return n
    else:
        return n+f(2*n)
def g(n):
    return f(n)/n
print(g(1000))
k=0
for n in range(1,1000001):
    if g(n)==g(1000):
        k+=1
print(k)