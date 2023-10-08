m = ''
for n in range(0, 1000):
    m = bin(n)[2::]
    m = m + m[-1]
    if m.count('1')%2 == 0:
        m = m + '0'
    else:
        m = m + '1'
    if m.count('1')%2 == 0:
        m = m + '0'
    else:
        m = m + '1'
    if int(m, 2) >97:
        print(n)


