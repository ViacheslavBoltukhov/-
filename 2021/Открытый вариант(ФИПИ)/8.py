from itertools import product

a = list(product('ВИШНЯ', repeat = 6))
k=0
for i in range(len(a)):
    if not a[i][0] == "Ш" and not a[i][5]=="И" and not a[i][5]=="Я" and a[i].count("В")<=1:
        k+=1

print(k)
        
