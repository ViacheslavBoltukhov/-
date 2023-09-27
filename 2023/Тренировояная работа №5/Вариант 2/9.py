f=open('09.csv').readlines()
k=0
for elem in f:
    x=sorted(list(map(int, elem.rstrip().split(';'))))
    if x[0]!=x[1] and len(x)!=len(set(x)) and x[-1]>3*(sum(x[:-1])/5):
        k+=1
print(k)