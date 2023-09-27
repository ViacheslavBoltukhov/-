n=list(map(int, open('17.txt').readlines()))
min17=10**9
coont=0
maxsum=0
for elem in n:
    if elem%17==0 and elem<min17:
        min17=elem
for i in range(len(n)-1):
    if n[i]%min17==0 or n[i+1]%min17==0:
        coont+=1
        maxsum=max(maxsum,n[i]+n[i+1])
print(coont,maxsum)