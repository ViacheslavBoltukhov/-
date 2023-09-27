s=open('24.txt').read().split('A')
max_len=0
for elem in s:
    if elem.count('E')>=3:
        max_len=max(max_len,len(elem))
print(max_len)