m={'А':'Б',
'Б':'ВЕ',
'В':'ГИ',
'Г':'И',
'Д':'АБЕ',
'Е':'ВЖЛ',
'Ж':'ВЛ',
'И':'МН',
'К':'Д',
'Л':'КД',
'М':'ЖЛ',
'Н':'М',
}
def f(s,e):
    global count
    if s=='Е' and len(e)>1:
        count+=1
    else:
        if e.count(s)>1:
            return
        for i in m[s]:
            f(i,e+i)
count=0
f('Е','Ж')
print(count)