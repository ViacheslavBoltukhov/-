a=[1]
b=[]
for i in range(10):
    for j in range(len(a)):
        b.append(2*a[j])
        b.append(2*a[j]+1)
    a=b
    b=[]
print(len(set(a)))
