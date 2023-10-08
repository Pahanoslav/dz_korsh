k = 0
c = []
for n in range(1, 10, 2):
    for ch in range(0, 10, 2):
        s = int('123' + str(n) + str(ch) + '56')
        if s % 206 == 0:
            c.append(s)
        for x in range(0, 10):
            s = int('123' + str(x) + str(n) + str(ch) + '56')
            if s % 206 == 0:
                c.append(s)
c = sorted(c)
for i in c:
    print(i//206, i)






