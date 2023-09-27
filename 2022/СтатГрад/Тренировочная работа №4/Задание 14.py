n=7*729**6+6*81**9+3**14-90
n9=''
while n:
    n9+=str(n%9)
    n//=9
print(len(n9))
n9=int(n9[::-1])
print(n9)
count=0
while n9:
    if n9%2==0:
        count+=1
    n9//=10
print(count)