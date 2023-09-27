s=open('24.txt').readline()
s=s[s.index('A')+1:].split('A')
count=0
for elem in s:
    if elem.count('B')>1 and len(elem)>9:
        count+=1
print(count)
