p=list(sorted(list(map(int, s.split())) for s in open('26.txt').readlines()[1:]))
p.append([0,0])
m_c_p=0
c_p=1
m_n=0
n_r=0
for i in range(len(p)-1):
    if p[i+1][1]!=p[i][1] and p[i+1][1]-p[i][1]==1:
        c_p+=1
    elif p[i+1][1]-p[i][1]>1:
        if c_p>m_c_p:
            m_c_p=c_p
            l=p[i][1]-c_p
            r=10000-p[i][1]
            t=p[i][0]-1
            d=10000-p[i][0]
            n_r=p[i][0]
            m_n=min(l,r,t,d)
        elif c_p==m_c_p:
            l = p[i][1] - c_p
            r = 10000 - p[i][1]
            t = p[i][0] - 1
            d = 10000 - p[i][0]
            if min(l,r,t,d)<m_n:
                m_n=min(l,r,t,d)
                n_r=p[i][0]
        c_p=1
print(n_r,m_n)