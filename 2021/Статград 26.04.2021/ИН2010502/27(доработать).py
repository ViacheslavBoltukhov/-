pairs = [tuple(map(int, pair.split())) for pair in open('27-B.txt').read().splitlines()]
result = [pair for pair in pairs if pair[1] %2 !=0]
sb = sum(max(pair) for pair in result)
sm = sum(min(pair) for pair in result)
print(f'сумма макс чисел - {sb}\nсумма мин чисел - {sm}\n')
minsumm = 999999
for pair in result:
    nres = result.copy()
    nres.remove(pair)
    nsb = sum(max(pair) for pair in nres)
    nsm = sum(min(pair) for pair in nres)
    if nsb %2 ==0 and nsm % 2!=0:
        minsumm = min(minsumm, sum(pair))
print(f'сумма макс чисел - {nsb}\nсумма мин чисел - {nsm}')
print(sb+sm - minsumm)
