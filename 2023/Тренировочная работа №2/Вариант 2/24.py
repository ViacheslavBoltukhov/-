f=open('24.txt').readline()
maxk=0
k=1
s='D'
for i in range(f.find('D')+1,f.rfind('D')):
    if f[i]!='D':
        s+=f[i]
    else:
        if s.count('O')<=2:
            k+=len(s)
        else:
            maxk=max(maxk,k)
            k=1
        s='D'
print(maxk)