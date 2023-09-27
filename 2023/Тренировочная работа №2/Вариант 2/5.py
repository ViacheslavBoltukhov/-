minr=10**9
for n in range(1,10000):
    r=bin(n)[2:]
    for i in range(3):
        s = sum(map(int, str(int(r,2))))
        if s%2==1:
            r+='1'
        else:
            r+='0'
    r=int(r,2)
    if r>2054:
        minr=min(r,minr)
print(minr)