dgts = [int(elem) for elem in open('26.txt').read().splitlines()]
ch = [elem for elem in dgts if elem%2==0]
nch = [elem for elem in dgts if elem%2!=0]
k = 0
ms = 0
for i in range(len(ch)):
    for j in range(i+1, len(ch)):
        if ch[i]+ch[j] in ch:
            k+=1
            ms = max(ms, ch[i]+ch[j])
for i in range(len(nch)):
    for j in range(i+1, len(nch)):
        if nch[i]+nch[j] in ch:
            k+=1
            ms = max(ms, nch[i]+nch[j])
print(k, ms)
                        
            
