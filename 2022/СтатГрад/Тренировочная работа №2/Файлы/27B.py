numbs=list(map(int, open('27-A.txt').read().splitlines()))
numbs.pop(0)
s=0
maxs=0
k=0
m=[2*10**9]*30
for elem in numbs:
    s+=elem
    if elem%2==0 and elem>0:
        k+=1
    if s<m[k%30]:
        m[k%30]=s
    if m[k%30]!=2*10**9:
        maxs=max(maxs,s-m[k%30])
print(maxs)
