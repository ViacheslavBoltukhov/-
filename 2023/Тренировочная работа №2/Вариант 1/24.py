s=open('24.txt').readline().split('F')
maxl=0
l=1
for elem in s:
    if elem.count('A')<=2:
        l+=len(elem)+1
    else:
        maxl=max(maxl,l)
        l=1
print(maxl)