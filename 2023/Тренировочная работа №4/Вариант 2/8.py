k=0
b='ЯРОСЛАВ'
gl='ЯОА'
sg='РСЛВ'
for b1 in b:
    for b2 in b:
        for b3 in b:
            for b4 in b:
                for b5 in b:
                    s=b1+b2+b3+b4+b5
                    kgl=0
                    ksg=0
                    a=set()
                    for elem in s:
                        if elem in sg:
                            ksg+=1
                        else:
                            kgl+=1
                        a.add(elem)
                    flag=True
                    for i in range(len(s)-1):
                        if s[i] in gl and s[i+1] in gl:
                            flag=False
                            break
                    if len(a)==5 and flag and ksg>kgl:
                        k+=1
print(k)