def m_find(s):
    mx, mn = 0, 9_999_999
    for i in range(2, s//2+1):
        if s % i == 0:
            mn = min(mn, i)
            mx = max(mn, i)
    return mn+mx


k = 1
i = 452_022
while k <= 5:
    if m_find(i) % 7 == 3:
        k += 1
        print(i, m_find(i))
    i += 1
