k = 0
nm = 999999999
for i in range(123456,234568):
    if i%(sum(int(elem) for elem in str(i)))==0:
          k+=1
          nm = min(nm, i)
print(k, nm)
