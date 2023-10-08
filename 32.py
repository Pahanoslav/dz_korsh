c = []
k = 0
p = []
for q in range(10):
    s = int('23' + str(q) + '5')
    c.append(s)

for q in range(10):
    for x1 in range(1, 10):
        s = int(str(x1) + '23' + str(q) + '5')
        c.append(s)

for q in range(10):
    for x1 in range(10):
        for x2 in range(1, 10):
            s = int(str(x2) + str(x1) + '23' + str(q) + '5')
            c.append(s)

for q in range(10):
    for x1 in range(10):
        for x2 in range(10):
            for x3 in range(1, 10):
                s = int(str(x3) + str(x2) + str(x1) + '23' + str(q) + '5')
                c.append(s)

for q in range(10):
    for x1 in range(10):
        for x2 in range(10):
            for x3 in range(10):
                for x4 in range(1, 10):
                    s = int(str(x4) + str(x3) + str(x2) + str(x1) + '23' + str(q) + '5')
                    c.append(s)

for q in range(10):
    for x1 in range(10):
        for x2 in range(10):
            for x3 in range(10):
                for x4 in range(10):
                    for x5 in range(1, 10):
                        s = int(str(x5) + str(x4) + str(x3) + str(x2) + str(x1) + '23' + str(q) + '5')
                        c.append(s)
p.append(12)
for x1 in range(1, 10):
    m = int('12' + str(x1))
    p.append(m)

for x1 in range(10):
    for x2 in range(10):
        m = int('12' + str(x2) + str(x1))
        p.append(m)


for i in c:
    for j in p:
        if i % j == 0:
            k += 1
            break
print(k)




