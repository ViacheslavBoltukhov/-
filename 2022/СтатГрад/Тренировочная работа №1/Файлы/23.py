def f(start,end):
    return f(start+1,end) + f(start*3,end) if start<end else start==end
print(f(2,28)*f(28,90))