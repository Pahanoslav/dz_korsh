c = []

for a1 in range(0, 100):
    for a2 in range(a1+1, 100):
        flag = 1
        x = -333
        while x < 333:
            x = x + 0.5
            if (((a1 <= x <= a2) <= (43 <= x <= 49)) or (44 <= x <= 53)) == False:
                flag = 0
        if flag == 1:
            c.append(a2-a1)
print(max(c))

