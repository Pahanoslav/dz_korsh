c = []
for q in range(0, 100):
    for i in range(0, 100):
        s = '14' + str(q) + '4' + str(i)
        s = int(s)
        if s % 217 == 0:
            c.append(s)
c.sort()
c = c[-7::]
for n in c:
    s = 0
    for j in range(1, n+1, 2):
        if n % j == 0:
            s += j
    print(n, s)
