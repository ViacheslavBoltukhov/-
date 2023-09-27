n=5*343**8+4*49**12+7**14-98
n7=''
while n:
    n7+=str(n%7)
    n//=7
for i in range(7):
    print(i,'-',n7.count(str(i)))
