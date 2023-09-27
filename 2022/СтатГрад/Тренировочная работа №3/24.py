strings=list(map(str, open('24.txt').readline().split('E')))
count=0
for string in strings:
    if string.count('F')==string.count('E')==0 and len(string)>=10:
        count+=1
print(count)