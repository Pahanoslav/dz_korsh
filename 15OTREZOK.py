c = []
for a1 in range(0, 1000):
    for a2 in range(a1, 1000):
        flag = 0
        for x in range(0, 1000):
            if (((295 <= x <= 400) <= (5 <= x <= 280)) or (not(a1 <= x <= a2) <= (375 <= x <= 450))) == False:
                flag = 1
        if flag == 0:
            print(a2-a1)

