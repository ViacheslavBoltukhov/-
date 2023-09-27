from itertools import combinations
for i in range(11,20):
    for elem in combinations(range(i*2),i):
        s=['1']*(i*2)
        for n in elem:
            s[n]='2'
        s='0'+''.join(s)+'0'
        while not ('00' in s):
            if '011' in s:
                s=s.replace('011','101',1)
            else:
                s=s.replace('01','40',1)
                s=s.replace('02','20',1)
                s=s.replace('0222','1401',1)
        if s.count('1')==8 and s.count('2')==13:
            print(s.count('4'))
            exit()