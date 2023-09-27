n=3*125**6+2*25**9+5**12-625
n5=''
while n:
    n5+=str(n%5)
    n//=5
print(n5.count('0'))