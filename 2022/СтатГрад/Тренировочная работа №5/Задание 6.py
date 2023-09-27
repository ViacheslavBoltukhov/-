s=2**29*3
print(s)
s=s//3
n=0
k=1
while s>k:
    s-=k
    k*=2
    n+=1
print(n)