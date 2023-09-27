from itertools import product
count=0
for i in range(3,10):
    for elem in product('1234',repeat=i):
        s=''.join(elem)
        if s.count('3')+s.count('4')==1:
            n=1
            for i in s:
                if i=='1' or i=='2':
                    n+=int(i)
                else:
                    n*=(int(i)-1)
            if n==10:
                count+=1
print(count)