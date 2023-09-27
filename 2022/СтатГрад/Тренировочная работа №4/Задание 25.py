k=0
count=0
while count<5:
   k+=1
   mk=7_000_000+k
   d=0
   a=[]
   for i in range(2,mk//2+1):
       if mk%i==0:
           a.append(i)
           d+=1
           mk//=i
   if d<3:
        print(k)
        print(*a,mk)
        count+=1