s = open('24.txt').read()
k = 1
kmax = 0
for i in range(len(s)-1):
    if s[i] == 'a' and s[i + 1] == 'd' or s[i] == 'd' and s[i + 1] == 'a':
        kmax = max(k, kmax)
        k = 1
    else:
        k += 1
print(kmax)
