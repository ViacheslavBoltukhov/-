lines = open('24.txt').read().splitlines()
mlen = 0
for line in lines:
    if line.count('A')<25:
        for i in range(65,91):
            mlen = max(mlen, line.rfind(chr(i))-line.find(chr(i)))
print(mlen)

            
        
