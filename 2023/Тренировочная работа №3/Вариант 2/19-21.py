def go(s1,s2):
    return s1+s2>=40
def win(s1,s2,m):
    if go(s1,s2): return False
    if s1<s2:
        return any(lose(s1+i,s2,m-1) for i in range(1,s1+1))
    return any(lose(s1,s2+i,m-1) for i in range(1,s2+1))
def lose(s1,s2,m):
    if go(s1, s2): return True
    if m==0: return False
    if s1 < s2:
        return all(win(s1 + i, s2, m) for i in range(1, s1 + 1))
    return all(win(s1, s2 + i, m) for i in range(1, s2 + 1))
ans19=10**9
for s1 in range(20):
    for s2 in range(20):
        if win(s1,s2,1):
            ans19=min(s1+s2,ans19)
s1=4
ans20=[]
ans21=[]
for s2 in range(1,36):
    if not win(s1,s2,1) and win(s1,s2,2):
        ans20.append(s2)
    if not lose(s1,s2,1) and lose(s1,s2,2):
        ans21.append(s2)
print(ans19)
print(max(ans20),min(ans20))
print(min(ans21))
