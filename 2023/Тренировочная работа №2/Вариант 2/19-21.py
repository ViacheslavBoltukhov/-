def go(s1,s2):
    return s1+s2>60
def win(s1,s2,m):
    if go(s1,s2): return False
    if s1<s2: return lose(s1+1,s2,m-1) or lose(s1+2,s2,m-1) or lose(s1*2,s2,m-1)
    return lose(s1,s2+1,m-1) or lose(s1,s2+2,m-1) or lose(s1,s2*2,m-1)
def lose(s1,s2,m):
    if go(s1,s2): return True
    if m==0: return False
    if s1<s2: return win(s1+1,s2,m) and win(s1+2,s2,m) and win(s1*2,s2,m)
    return win(s1,s2+1,m) and win(s1,s2+2,m) and win(s1,s2*2,m)
s1=8
ans19=[]
ans20=[]
ans21=[]
for s2 in range(1,53):
    if lose(s1,s2,1):
        ans19.append(s2)
    if not win(s1,s2,1) and win(s1,s2,2):
        ans20.append(s2)
    if not lose(s1,s2,1) and lose(s1,s2,2):
        ans21.append(s2)
print(min(ans19))
print(min(ans20),max(ans20))
print(max(ans21))
