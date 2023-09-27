def f(s,e):
    if s<e:
        if s==11 or s==15:
            return 0
        return f(s+1,e) + f(s*2,e) + f(s+3,e)
    else:
        return s==e
print(f(2,8)*f(8,20))