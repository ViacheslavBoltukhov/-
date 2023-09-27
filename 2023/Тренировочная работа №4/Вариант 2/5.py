m=[]
for k in int(bin(876544)[2:-3],2), int(bin(1234567899)[2:-3],2):
    for n in range(k-5,k+5):
        r=bin(n)[2:]
        for i in range(3):
            x=int(r,2)
            kch=0
            knch=0
            while x:
                if x%2==0:
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
        r=int(r,2)
        if r>=876544 and r<=1234567899:
            m.append(n)
print(max(m)-min(m)+1)