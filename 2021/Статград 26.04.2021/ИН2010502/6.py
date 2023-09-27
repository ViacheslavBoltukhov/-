from itertools import product
k = 0
a = product("РУСЛАН", repeat = 5)
for tpl in a:
    if tpl.count('У')<=1 and tpl.count("А") <= 1:
        k+=1
print(k)
