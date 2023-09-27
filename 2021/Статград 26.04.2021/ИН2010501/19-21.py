s1, end = 6, 79
o1, o2 = 1, 3
def game_over(n1, n2):
    return n1 + n2 >= end
def win(n1, n2, move):
    if game_over(n1, n2): return False
    return lose(n1 + o1, n2, move - 1) or \
           lose(n1 * o2, n2, move - 1) or \
           lose(n1, n2 + o1, move - 1) or \
           lose(n1, n2 * o2, move - 1)
def lose(n1, n2, move):
    if game_over(n1, n2): return True
    if move == 0: return False
    return win(n1 + o1, n2, move) and \
           win(n1 * o2, n2, move) and \
           win(n1, n2 + o1, move) and \
           win(n1, n2 * o2, move)


from math import *

ans19 = ceil((end - s1) / 9)
ans20 = []
ans21 = 0
for s2 in range(1, end - s1):
    if win(s1, s2, 2) and not win(s1, s2, 1):
        ans20.append(s2)
    if lose(s1, s2, 1):
        ans21 = s2
print(ans19)
print(*ans20)
print(ans21)
