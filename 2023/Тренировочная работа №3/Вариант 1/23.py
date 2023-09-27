def f(s,e,k):
    if s<e:
        if k==0:
            return f(s+1,e,0)+f(s+2,e,0)+f(s*2,e,1)+f(s*3,e,1)
        else:
            return f(s+1,e,1)+f(s+2,e,1)
    else:
        return s==e
def p(s,e):
    if s<e:
        return p(s+1,e)+p(s+2,e)
    else:
        return s==e
print(f(1,11,0)-p(1,11))