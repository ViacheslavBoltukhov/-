def f(n,l):
    global count
    if n==start and len(l)>1:
        print(l)
        count+=1
    else:
        if l.count(n)>1:
            return
        for i in m[n]:
            f(i,l+i)
m={'А':'Б',
   'Б':'В',
   'В':'ЕГЖ',
   'Г':'ДЕ',
   'Д':'ЕЖК',
   'Е':'Ж',
   'Ж':'ЗН',
   'З':'ДКЛ',
   'К':'Л',
   'Л':'М',
   'М':'АН',
   'Н':'АБВ',
   }
count=0
start='Ж'
f(start,start)
print(count)
