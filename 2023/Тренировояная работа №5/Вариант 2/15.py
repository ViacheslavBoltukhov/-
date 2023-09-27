p=[x for x in range(13,32)]
q=[x for x in range(19,81)]
r=[x for x in range(48,115)]
a=[]
for x in range(1,1000):
    if not(not(x in q) or (x in p) or (x in r)):
        a.append(x)
print(len(a)+1)