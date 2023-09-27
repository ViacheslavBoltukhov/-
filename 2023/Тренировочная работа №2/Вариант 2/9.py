f=open('09.csv')
count=0
for elem in f:
    m=list(map(int, elem.split(';')))
    s=set(m)
    if len(m)==len(s):
        s_ch,s_nch,k_ch,k_nch=0,0,0,0
        for n in s:
            if n%2==0:
                k_ch+=1
                s_ch+=n
            else:
                k_nch+=1
                s_nch+=n
        if k_ch>k_nch and s_ch<s_nch:
            count+=1
print(count)
