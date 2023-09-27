'''Файл А(Переборный алгоритм)'''
n=list(map(int, open('27-A.txt').readlines()))
count=0
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if (n[i]+n[j])%4==0 and (n[i]*n[j])%6561==0:
            count+=1
print(count)