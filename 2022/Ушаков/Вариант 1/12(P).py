s=83*'7'
while '77777' in s or '222' in s:
    if '77777' in s:
        s=s.replace('77777','22',1)
    else:
        s=s.replace('222','2',1)
print(s)