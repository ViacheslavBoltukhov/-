'''F(0) = 0;
F(n) = F(n/2), если n > 0 и при этом n чётно;
F(n) = 1 + F(n – 1), если n нечётно.
Сколько существует таких чисел n, что 1 ≤ n ≤ 1000 и F(n) = 3'''
def F(n):
    if n==0:
        return 0
    if n>0 and n%2==0:
        return F(n//2)
    else:
        return 1 + F(n-1)
k = 0
for i in range(1,1001):
    if F(i)==3:
        k+=1   
print(k)
