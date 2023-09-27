numb=list(map(int, open('27-B.txt').readlines()[1:]))
n2,n3,n61,n62=0,0,0,0
for elem in numb:
    if elem%6==0:
        if elem>n61:
            n61,n62=elem,n61
        elif elem>n62:
            n62=elem
    if elem%2==0 and elem%3!=0 and elem>n2:
        n2=elem
    if elem%3==0 and elem%2!=0 and elem>n3:
        n3=elem
print(n2,n3,n61,n62)
print(max(n2*n3,n2*n61,n3*n61,n61*n62))