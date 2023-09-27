def f(n):
    if n==0: return 0
    if n%2==0: return f(n//2)
    if n%2==1: return 1+f(n-1)
count=0
for x in range(1,501):
    if f(x)==3:
        count+=1
print(count)
