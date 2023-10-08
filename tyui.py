count = 0
for i in range(245690, 245756):
    count += 1
    c = []
    for j in range(2, i):
        if i % j == 0:
            c.append(j)
    if len(c) == 0:
        print(count, i)
