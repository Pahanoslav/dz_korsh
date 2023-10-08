c = []
for a in range(0, 1000):
    flag = 1
    for y in range(0, 1000):
        for x in range(0, 1000):
            if ((7*y + 5*x < 1000) or (x < y) or (a < x)) == False:
                flag = 0
    if flag == 1:
        print(a)
