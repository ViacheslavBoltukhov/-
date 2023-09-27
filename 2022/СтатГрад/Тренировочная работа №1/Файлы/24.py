s=open('24.txt').read()
max_l=0
k=0
l=0
for elem in s:
    if elem=='A':
        max_l = max(l+k, max_l)
        k=l-1
        l=0
    l+=1
print(max_l)