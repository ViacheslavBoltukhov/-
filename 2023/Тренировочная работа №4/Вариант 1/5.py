n=int(input())
r=bin(n)[2:]
for i in range(3):
    x=int(r,2)
    kch=0
    knch=0
    while x:
        if (x%10)%2==0:
            kch+=1
        else:
            knch+=1
        x//=10
    if kch==knch:
        r+=str(n%2)
    elif kch>knch:
        r+='1'
    else:
        r+='0'
print(r,int(r,2))