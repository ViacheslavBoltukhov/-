m=[0]*41
m[1]=1
for i in range(2,41):
    if str(i).count('3')==0:
        if i%2==0:
            m[i]=m[i-1]+m[i//2]
        else:
            m[i]=m[i-1]
print(m)
print(m[40])