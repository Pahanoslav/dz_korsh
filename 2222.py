c = []
for a1 in range(0, 1000):
    for a2 in range(a1, 1000):
        flag = 1
        for x in range(0, 1000):
            if ((25 <= x <= 120) < (((not(1 <= x <= 40)) and (25 <= x <= 120)) <= (a1 <= x <= a2))) == False:
                flag = 0
        if flag == 1:
            c.append(a2-a1)
print(sorted(c))
