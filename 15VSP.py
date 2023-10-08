c = []
for a1 in range(0, 200):
    for a2 in range(a1+1, 200):
        flag = 1
        for x in range(0, 100):
            if ((a1 <= x <= a2) <= (10 <= x <= 15)) == ((10 <= x <= 20) <= (5 <= x <= 15)):
                c.append(a2-a1)
print(c)
