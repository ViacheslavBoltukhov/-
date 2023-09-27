k=0
mk=0
for l in 0,1:
    s=open('24-204.txt').readline()[l:]
    for i in range(0,len(s),2):
        if s[i:i+2]=='AA' or s[i:i+2]=='CC' :
            k+=1
        else:
            mk=max(k,mk)
            k=0
print(mk)
s = open('24-204.txt').readline().strip()

mc = 0
for st in (0, 1):
    c = 0
    for i in range(st, len(s), 2):
        if s[i:i+2] in ('AA', 'CC'):
            c += 1
        else:
            mc = max(mc, c)
            c = 0

print( mc )