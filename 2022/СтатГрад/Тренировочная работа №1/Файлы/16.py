def f(n):
    if n==0: return 0
    if n%2==0: return f(n/2)
    return 1+f(n-1)
count=0
for i in range(1,501):
    if f(i)==8:
        count+=1
print(count)