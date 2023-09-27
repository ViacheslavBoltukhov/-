def f(s,e,k1,k2):
    if s<e:
        if k1==k2==0 or k1!=k2:
            return f(s+1,e,k2,1)+f(s*2,e,k2,2)
        if k1==k2==1:
            return f(s*2,e,k2,2)
        if k1==k2==2:
            return f(s+1,e,k2,1)
        return 0
    else:
        return s==e
print(f(1,16,0,0))
