from itertools import *
t=[[0,0,0,15,29,31,0,0],
   [0,0,18,0,30,0,25,0],
   [0,18,0,0,0,0,33,24],
   [15,0,0,0,0,21,0,0],
   [29,30,0,0,0,14,0,27],
   [31,0,0,21,14,0,23,0],
   [0,25,33,0,0,23,0,12],
   [0,0,24,0,27,0,12,0]]
g = 'АБ БВ ВГ ГИ ИЖ ЖЕ ЕД ДА ДБ БЕ ЕВ ЖГ ВИ'
m=list(map(str, (g + ' ' + g[::-1]).split()))
print(m)
def i(v): return [p.index(c) for c in v]
def f(x,y): x,y = i(x+y); return t[x][y]
p='ДЖГАЕБВИ'
for x in p:
    for y in p:
        if (f(x,y)>0)!=(x+y in m):
            print(x+y,f(x,y)>0,(x+y in m),(f(x,y)>0)==(x+y in m))
'''for p in permutations(set(g)-{' '}):
    if all((f(x,y)>0)==(x+y in m) for x in p for y in p):
        print(*p)'''
