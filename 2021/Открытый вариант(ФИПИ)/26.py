s = 99990
cargo = sorted(tuple(map(int, open('26(edited).txt').read().splitlines())))
k, m, i = 0, 0, 0
while s - cargo[i] >= 0:
    s -= cargo[i]
    k += 1
    m = cargo[i]
    if i < len(cargo):
        i += 1
    else:
        break
else:
    for j in range(i+1, len(cargo)):
        if s - m + cargo[j] >= 0:
            s = s - m + cargo[j]
            m = cargo[j]
print(k, m)
