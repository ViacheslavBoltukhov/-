def GameOver(n):
    return n>=47
def Win(n,moves):
    if GameOver(n): return False
    return Lose(n+1,moves-1) or Lose(n*3,moves-1)
def Lose(n,moves):
    if GameOver(n): return True
    if moves==0: return False
    return Win(n+1,moves) and Win(n*3,moves)
from math import *
ans19=[]
ans20=[]
ans21=[]
for n in range(1,47):
    if Lose(n,1):
        ans19.append(n)
    if Win(n,2) and not Win(n,1):
        ans20.append(n)
    if Lose(n,2) and not Lose(n,1):
        ans21.append(n)
print('19 -',*ans19)
print('20 -',*ans20)
print('21 -',*ans21)


