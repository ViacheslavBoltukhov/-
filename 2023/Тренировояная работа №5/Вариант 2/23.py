def f(s,e):
    if s<e:
        if s==13 or s==17:
            return 0
        return f(s+1,e)+f(s+3,e)+f(s*2,e)
    else:
        return s==e
print(f(3,10)*f(10,22))