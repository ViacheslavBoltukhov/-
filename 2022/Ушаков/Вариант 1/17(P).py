count=0
maximum=0
for i in range(1316,9965):
    if i%5==0 and i%3!=0 and i%7!=0 and i%11!=0 and i%25!=0:
        count+=1
        maximum=max(maximum,i)
print(count,maximum)