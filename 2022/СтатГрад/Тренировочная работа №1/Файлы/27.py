#Запишем все числа из файла в массив numbs
numbs=list(map(int, open('27-A.txt').read().splitlines()))
numbs.pop(0)    #Удалим первый элемент массива т.к это количество чисел для обработки
#Пробежим массив numbs и посчитаем количество чётных элементов
k=0
for i in range(len(numbs)):
    if numbs[i]%2==0:
        k+=1
n=k%10  #Количетво чётных элементов которые надо удалить из суммы всех чисел
sum_numb_r=[]
sum_numb_l=[]
nr=0
nl=0
#Пробежим массив numbs и составим суммы слева направо и справа налево до 1,2..n чётного числа
for i in range(len(numbs)):
    if numbs[i]%2==0:
        sum_numb_l.append(sum(numbs[:i+1]))
        nl+=1
        if nl==n:
            break
for i in range(len(numbs)-1,-1,-1):
    if numbs[i]%2==0:
        sum_numb_r.append(sum(numbs[-1:i-1:-1]))
        nr+=1
        if nr==n:
            break
sum_min=[]
#Составим все возможные непрерывные цепочки сумм с n чётными элементами
sum_min.append(sum_numb_r[-1])
sum_min.append(sum_numb_l[-1])
for i in range(n-1):
    sum_min.append(sum_numb_l[i]+sum_numb_r[n-i-2])
#Вычтем из суммы всех элементов сумму минимальной непрерывной цепочки из n чётных элементов
print(sum(numbs)-min(sum_min))