m={'А':'ВД',
'Б':'АД',
'В':'Г',
'Г':'ДЖ',
'Д':'ВЖ',
'Е':'БДЖ',
'Ж':'МКИ',
'И':'Е',
'К':'И',
'Л':'Г',
'М':'ЛК',
   }
def l(s,e):
    global count
    if s=='Д' and len(e)>1:
        count+=1
    else:
        if e.count(s)>1:
            return
        for i in m[s]:
            l(i,e+i)
count=0
l('Д','Д')
print(count)

