'''Рассматривается множество целых чисел, принадлежащих числовому отрезку [12972; 89322],
которые при делении на 13 дают остаток 7, при этом не делятся ни на 7, ни на 11. Найдите
наибольшее из таких чисел и их количество. В ответе укажите два числа друг за другом без
разделительных знаков — сначала количество найденных чисел, затем наибольшее найденное
число.
'''

count = 0
maximum = 0
for x in range(12972, 89323):
    if x % 13 == 7 and x % 7 != 0 and x % 13 != 0:
        count += 1
        maximum = x
print(count,maximum)