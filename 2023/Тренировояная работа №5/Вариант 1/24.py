f=open('24.txt').readline()
a=['ABC','ACB','BAC','BCA','CAB','CBA']
k=0
maxk=0
for i in range(len(f)-2):
    if f[i:i+3] not in a:
        k+=1
    else:
        maxk=max(maxk,k-2)
        k=0
print(maxk)