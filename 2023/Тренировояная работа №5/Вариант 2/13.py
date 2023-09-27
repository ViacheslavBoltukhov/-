m={'А':'Б',
'Б':'ВЕ',
'В':'ГИЖ',
'Г':'И',
'Д':'АБ',
'Е':'ДЛ',
'Ж':'ЕМ',
'И':'ЖН',
'К':'Д',
'Л':'КД',
'М':'ЕЛИ',
'Н':'М',
}
def f(e,s):
    global count
    if e=='А' and len(s)>1:
        count+=1
    else:
        if s.count(e)>1:
            return
        else:
            for i in m[e]:
                f(i,s+i)
count=0
f('Н','А')
print(count)