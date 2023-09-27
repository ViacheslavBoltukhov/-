def f(n):
    if n==0: return 0
    if n%3!=0: return f(n-1)+1
    return f(n//3)
n1=1_200_000_000
n2=1_600_000_000
r1=''
r2=''
while n1:
    r1+=str(n1%3)
    n1//=3
r1=r1[::-1]
while n2:
    r2+=str(n2%3)
    n2//=3
r2=r2[::-1]
print(r1)
print(r2)
print(int('10'+'2'*(len(r1)-2),3))
print(f(1549681955))