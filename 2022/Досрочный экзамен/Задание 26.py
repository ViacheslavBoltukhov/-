n=list(list(map(int, s.split())) for s in open('26.txt').readlines())
n.pop(0)
n.sort()
print(n[:10])