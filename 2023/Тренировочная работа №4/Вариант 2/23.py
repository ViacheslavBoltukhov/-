def f(s,e,sl,pr):
    if s<e:
        if sl==pr==0:
            return f(s+1,e,1,0) + f(s+2,e,1,0) + f(s*2,e,0,1) + f(s*3,e,0,1)
        if sl==1:
            return f(s*2,e,0,1) + f(s*3,e,0,1)
        if pr==1:
            return f(s+1,e,1,0) + f(s+2,e,1,0)
    else:
        return s==e
print(f(1,24,0,0))