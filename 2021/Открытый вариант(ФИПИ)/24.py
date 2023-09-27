line = open('D:\\Users\\User\\Desktop\\Programs\\Python\\24.txt').readline()
line = line.replace('XZZY', ' ').split()
print(max(len(row) for row in line))