s='0'+'22'*4+'211'*9+'1'*5+'0'
n=s.count('2')
while not('00' in s):
    s=s.replace('021','102',1)
    s=s.replace('022','301',1)
    s=s.replace('02','20',1)
    s=s.replace('01','10',1)
print(s.count('1'))
print(s.count('2'))
print(s.count('3'))
print(n)