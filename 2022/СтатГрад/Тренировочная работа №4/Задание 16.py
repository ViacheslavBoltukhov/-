def f(a,b):
    if a==0: return b
    return f(a//10,10*b+(a%10))
print(f(4623618421,0))