def f(s,e):
    return f(s + 1, e) + f(s * 2, e)  if s < e else s == e
print(f(1,10)*f(10,20))