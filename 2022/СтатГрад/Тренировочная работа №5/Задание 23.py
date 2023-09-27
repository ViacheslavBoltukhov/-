def f(start,end):
    return f(start+1,end)+f(start*10+1,end) if start<end else start==end
print((f(1,333)))