def f(star,end,count):
    if star<end:
        if count<2:
            count+=1
            return f(star+1,end,0)+f(star*2,end,count)
        else:
            return f(star+1,end,count)
    else: return star==end
print(f(1,11,0))