'''Полусовершенные числа'''

'''Нахождение всех множителей числа'''
def divisors(n):
    v = set()
    for i in range(1, int(n**0.5) + 1):
        if (n % i == 0):
            v.add(i)
            v.add(n // i)
    v=sorted(v)
    return v[:-1]

'''Проверка на полусовершенность'''
def check(n):
    v = []
    v = divisors(n)
    r = len(v)
    # Подмножество для проверки
    subset = [[0 for i in range(n + 1)]
              for j in range(r + 1)]
    # 1-ый столбец "Истина"
    for i in range(r + 1):
        subset[i][0] = True

    # 1-ая строка "Ложь", кроме 0-ой позиции
    for i in range(1, n + 1):
        subset[0][i] = False

    # Цикл для определения полусовершенности
    for i in range(1, r + 1):
        for j in range(1, n + 1):
            # суммирование делителей числа
            if (j < v[i - 1]):
                subset[i][j] = subset[i - 1][j]
            else:
                subset[i][j] = (subset[i - 1][j] or
                                subset[i - 1][j - v[i - 1]])
    #Проверка на полусовепшенность
    if (subset[r][n]) == 0:
        return False
    else:
        return True

k=0
for i in range(2,2001):
    if (check(i)):
        k+=1
print(k)