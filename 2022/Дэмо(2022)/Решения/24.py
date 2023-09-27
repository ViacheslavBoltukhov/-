s=[str(elem) for elem in map(str, open('24.txt').read().split('PP'))]
m=max(len(s[0]),len(s[len(s)-1]))+1
for i in range(1,len(s)-1):
    m=max(m,len(s[i])+2)
print(m)