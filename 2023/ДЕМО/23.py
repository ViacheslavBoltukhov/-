def f(start,end):
    if start==17:
        return 0
    if start<end:
        return f(start+1,end)+f(start*2,end)
    else:
        return start==end
print(f(1,10)*f(10,35))