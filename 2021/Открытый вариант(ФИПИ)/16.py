'''F(n) = 1 при n = 1; 
F(n) = n + F(n − 1), если n чётно; 
F(n) = 2 × F(n − 2), если n > 1 и при этом n нечётно. 
Чему равно значение функции F(24)?'''


def F(n):
    if n==1: return 1
    if n%2==0: return n+F(n-1)
    else: return 2*F(n-2)
print(F(24))
