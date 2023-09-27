#Создадим двумерный массив, каждый элемент которого массив в котором
#первый элемент стоимость детали,а второй её тип
goods=list(list(map(str, s.split())) for s in map(str, open('26.txt').read().splitlines()))
#В первом элементе массива находится информация о количестве деталий и имеющейся у нас суммы
#записываем эти данные в переменные count и ost, а затем удаляем из массива и сортируем его
count,ost=int(goods[0][0]),int(goods[0][1])
goods.pop(0)
goods=sorted(goods)
count_a=0   #Количество изделий типа А
numb_last=0 #Номер последнего купленного изделия
#Определим сколько останется денег и сколько изделий типа А можно купить,
# если покупать исходя из стоимисти изделия(т.е самые дешёвые)
while ost-int(goods[numb_last][0])>=0:
    ost-=int(goods[numb_last][0])
    if goods[numb_last][1]=='A':
        count_a+=1
    numb_last+=1
numb_b=numb_last #Номер изделия типа В который можно заменить изделием типа А
#Определим сколько дорогих изделий типа В(которые мы купили) можно заменить более
#дорогими изделиями типа А исходя из оставшейся суммы денег и заменим их
for numb_b in range(numb_b,-1,-1):
    if goods[numb_b][1]=='B':
        while goods[numb_last][1]!='A':
            numb_last+=1
        if ost+int(goods[numb_b][0])-int(goods[numb_last][0])>=0:
            ost=ost+int(goods[numb_b][0])-int(goods[numb_last][0])
            count_a+=1
        numb_last+=1
print(count_a,ost)