s=open('24.txt').readline()
s=s.replace('A','1').replace('O','1')
s=s.replace('B','0').replace('C','0').replace('D','0').replace('F','0')
s=s.replace('01','x')
l=0
maxl=0
for i in range(len(s)):
    if s[i]=='x':
        l+=1
    else:
        maxl=max(maxl,l)
        l=0
print(max(maxl,l))