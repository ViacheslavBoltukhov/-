triplets = [sorted(tuple(map(int, triplet.split()))) for triplet in open('27_B(E).txt')]
print(triplets[:10])
summ = sum(triplet[2] for triplet in triplets)
print(summ/109)
if summ % 109 != 0:
    print(summ)
else:
    mr = 10_001
    for triplet in triplets:
        if (triplet[2] - triplet[1]) % 109 != 0:
            mr = min(triplet[2] - triplet[1], mr)
        if (triplet[2] - triplet[0]) % 109 != 0:
            mr = min(triplet[2] - triplet[0], mr)
    print(summ - mr)