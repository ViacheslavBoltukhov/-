def go(s1,s2):
    return s1>=40 or s2>=40
def win(s1,s2,m):
    if go(s1,s2): return False
    if s1==s2: return lose(s1+1,s2,m-1) or lose(s1+2,s2,m-1) or lose(s1+3,s2,m-1)
    if s1>s2: return lose(s1+1,s2,m-1) or lose(s1+2,s2,m-1) or lose(s1+3,s2,m-1) or lose(s1,s2*2,m-1)
    if s1<s2: return lose(s1,s2+1,m-1) or lose(s1,s2+2,m-1) or lose(s1,s2+3,m-1) or lose(s1*2,s2,m-1)
def lose(s1,s2,m):
    if go(s1,s2): return True
    if m==0: return False
    if s1==s2: return win(s1+1,s2,m) and win(s1+2,s2,m) and win(s1+3,s2,m)
    if s1>s2: return win(s1+1,s2,m) and win(s1+2,s2,m) and win(s1+3,s2,m) and win(s1,s2*2,m)
    if s1<s2: return win(s1,s2+1,m) and win(s1,s2+2,m) and win(s1,s2+3,m) and win(s1*2,s2,m)
ans19=10**10
for s1 in range(1,40):
    for s2 in range(1,40):
        if win(s1,s2,1):
            ans19=min(ans19,s1+s2)
ans20=[]
ans21=[]
for s2 in range(1,40):
    if not win(11,s2,1) and win(11,s2,2):
        ans20.append(s2)
    if not lose(31,s2,1) and lose(31,s2,2):
        ans21.append(s2)
print(ans19)
print(min(ans20),max(ans20))
print(*ans21)