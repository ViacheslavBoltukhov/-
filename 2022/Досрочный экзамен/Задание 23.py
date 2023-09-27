def f(s,e):
    return f(s+2,e)+f(s*2,e) if s<e else s==e
print(f(1,16)*f(16,52))