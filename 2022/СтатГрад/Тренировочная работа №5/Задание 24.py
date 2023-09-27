s=open('24.txt').readline().replace('A','1').replace('B','1').split('1')
maxl=0
for i in range(len(s)-3):
    maxl=max(maxl,len(s[i]+s[i+1]+s[i+2]+s[i+3])+3)
print(maxl)