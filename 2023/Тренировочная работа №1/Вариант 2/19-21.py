def GameOver(s):
    return s>=151
def Win(s,moves):
    if GameOver(s): return False
    if s%3==2:
        return Lose(s+2,moves-1) or Lose(s*2,moves-1)
    elif s%3==1:
        return Lose(s+1,moves-1) or Lose(s*2,moves-1)
def Lose(s,moves):
    if GameOver(s): return True
    if moves==0: return False
    if s%3==2:
        return Win(s+2,moves) and Win(s*2,moves)
    elif s%3==1:
        return Win(s+1,moves) and Win(s*2,moves)
ans19=[]
ans20=[]
ans21=[]
for s in range(1,150):
    if s%3!=0:
        if Lose(s,1):
            ans19.append(s)
        if Win(s,2) and not Win(s,1):
            ans20.append(s)
        if Lose(s,2) and not Lose(s,1):
            ans21.append(s)
print('19 -',*ans19)
print('20 -',*ans20)
print('21 -',*ans21)