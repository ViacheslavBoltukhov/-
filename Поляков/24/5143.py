s=list(map(str, open('24-200.txt').read().splitlines()))
k=0
for elem in s:
    a=elem.split('.')
    if a[0]=='195' and a[1][0]=='2' and a[3]=='14':
        k+=1
print(k)