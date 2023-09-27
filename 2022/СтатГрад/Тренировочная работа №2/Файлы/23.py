def f(s,e):
    return f(s+1,e)+f(s+2,e)+f(s*3,e) if s<e else s==e
print(f(1,8)*f(8,15))