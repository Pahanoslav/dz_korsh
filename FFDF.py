r = ''
for n in range(0, 1000):
    r = r + bin(n)[2::]
    r = r.split()
    if sum(r) % 2 == 0:
        r = r + '0'
        r = '10' + r[::2]
    else:
        r = r + '1'
        r = '1' + r[::2]

    if int(r, 2) > 40:
        print(n)


