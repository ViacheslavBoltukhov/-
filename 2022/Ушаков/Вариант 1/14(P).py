n=9**200+3**100-7
res=''
while n:
    res+=str(n%3)
    n//=3
print(res.count('2'))