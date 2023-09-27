from itertools import permutations
a=[''.join(x) for x in permutations('XYZ',3)]
s=open('24.txt').readline()+'XYZ'
l=0
ml=0
for i in range(len(s)-2):
    if s[i:i+3] in a:
        ml=max(ml,l)
        l=-2
    else:
        l+=1
print(ml)