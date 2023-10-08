a = 4311744496
m = ''
while a != 0:
    m = m + str(a % 2)
    a = a // 2
print(m.count('1'))
