m={'А':'Б',
'Б':'В',
'В':'ГЖЕ',
'Г':'И',
'Д':'А',
'Е':'АД',
'Ж':'ГЕ',
'И':'МН',
'К':'ДЖ',
'Л':'КЖ',
'М':'ЖЛ',
'Н':'М',
}
def f(s,e):
    global count
    if s=='Ж' and len(e)>1:
        count+=1
    else:
        if e.count(s)>1:
            return
        for i in m[s]:
            f(i,e+i)
count=0
f('Ж','Ж')
print(count)