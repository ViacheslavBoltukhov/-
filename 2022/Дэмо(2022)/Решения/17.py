a=[int(elem) for elem in open('17.txt')]
m_s=-20000
s=0
count=0
for i in range(len(a)-1):
    if a[i]%3==0 or a[i+1]%3==0:
        count+=1
        if a[i]+a[i+1]>m_s:
            m_s=a[i]+a[i+1]
print(count,m_s)