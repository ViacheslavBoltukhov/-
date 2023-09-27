from copy import deepcopy

nums = tuple(map(int, open('26 (2).txt').read().splitlines()))
chn = tuple(filter(lambda elem: elem % 2 == 0, deepcopy(nums)))
k = 0
msr = 0
for i in range(len(chn)-1):
    for j in range(i+1, len(chn)):
        if (chn[i] + chn[j])//2 in nums:
            k+=1
            msr = max(msr, (chn[i] + chn[j])//2)
print(k, msr)
          
