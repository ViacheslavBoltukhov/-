s=open('24-191.txt').readline().strip().split('A')
s.pop(0)
k=0
for elem in s:
    if elem.count('B')>0:
        a=elem.split('B')[0]
        if len(a)>=18:
            if a.count('F')==2:
                print(a)
                k+=1
print(k)
