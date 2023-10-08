c = []
for a in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        if ((x % 13 == 0) <= (not(40 <= x <= 60)) or (a < x +20)) == False:
            flag = 0
    if flag == 1:
        c.append(a)
print(sorted(c))
