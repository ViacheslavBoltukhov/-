s=open('24.txt').readline()
s=s[s.index('A'):]
counta=0
countb=0
count=0
count_grup=0
for elem in s:
    count+=1
    if elem=='A':
        counta+=1
    if counta==1 and elem=='B':
        countb+=1
    if counta==2:
        if count>11 and countb>1:
            count_grup+=1
        count=1
        counta=1
        countb=0
print(count_grup)