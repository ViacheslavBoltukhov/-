def f(s,e,n):
    if s<e:
        if n==0:
            return f(s+1,e,0)+f(s+2,e,0)+f(s*2,e,1)
        if n==1:
            return f(s+1,e,0)+f(s+2,e,0)
    else:
        return s==e
print(f(1,11,0))