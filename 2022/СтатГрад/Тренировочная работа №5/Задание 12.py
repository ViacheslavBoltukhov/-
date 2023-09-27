s='0'+5*'1'+12*'21'+'0'
print(s.count('2'))
while not('00' in s):
    s=s.replace('02','20',1)
    s=s.replace('03','30',1)
    s=s.replace('011','1031',1)
    s=s.replace('01','102',1)
print(s.count('1'))
print(s.count('2'))
print(s.count('3'))