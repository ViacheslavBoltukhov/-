'''Переборный вариант для Файла А'''
fail=open('27_A.txt')
n=int(fail.readline())
p=[]
for i in range(n):
    s,count=map(int, fail.readline().split())
    p.append([s,count//36 if count%36==0 else count//36+1])
min_sum=10**20
sum=0
for i in range(n):
    for j in range(n):
        sum+=abs(p[i][0]-p[j][0])*p[j][1]
    min_sum=min(min_sum,sum)
    sum=0
print(min_sum)
'''Вариант для файла В'''
fail=open('27_B.txt')
n=int(fail.readline())
p=[]
for i in range(n):
    s,count=map(int, fail.readline().split())
    p.append([s,count//36 if count%36==0 else count//36+1])
p_count=[0]*n
p_count[0]=p[0][1]
for i in range(1,n):
    p_count[i]=p_count[i-1]+p[i][1]# Кол-во контейнеров в каждом пункте
max_count=p_count[-1]#Всего контейнеров
sum=0
for i in range(n):
    sum+=abs(p[i][0]-p[0][0])*p[i][1]# Стоимость при движении из начального пункта
min_sum=sum
for i in range(1,n):# пересчитываем стоимость при движении НЕ из начального пункта
    l=p[i][0]-p[i-1][0]# На какое расстояние  сдвигаемся
    sum=sum+l*p_count[i-1]-l*(max_count-p_count[i-1])# Для пунктов слева стоимость доставки увеличивается
    # А для пунктов справа уменьшается
    min_sum=min(min_sum,sum)
print(min_sum)