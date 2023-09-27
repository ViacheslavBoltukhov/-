def gameover(s):
    return 40<s<51
def win(s,move):
    if gameover(s): return False
    if s*2>50: return lose(s+1,move-1) or lose(s+2,move-1)
    return lose(s+1,move-1) or lose(s+2,move-1) or lose(s*2,move-1)
def lose(s,move):
    if gameover(s): return True
    if move==0: return False
    if s*2>50: return win(s+1,move) and win(s+2,move)
    return win(s+1,move) and win(s+2,move) and win(s*2,move)
ans19=[]
ans20=[]
ans21=[]
for s in range(1,41):
    if not lose(s,1) and lose(s,2):
        ans19.append(s)
    if not lose(s,1) and not lose(s,2) and lose(s,3):
        ans20.append(s)
    if not win(s,1) and win(s,2):
        ans21.append(s)
print(ans19)
print(ans20)
print(ans21)