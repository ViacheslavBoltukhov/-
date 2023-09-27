def f(s,e):
    if s<e:
        if str(s).count('5')==0:
            return f(s+1,e)+f(s*2,e)
        else:
            return 0
    else:
        return s==e
print(f(1,60))