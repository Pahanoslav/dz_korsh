p = ''
for q in range(0, 10):
    for q1 in range(0, 10):
        p = int('1' + str(q) + '0' + str(q1) + '6' + '39')
        if p % 131 == 0:
            print(p, p//131)
        for s in range(0, 10):
            p = int('1' + str(q) + '0' + str(q1) + '6' + str(s) + '39')
            if p % 131 == 0:
                print(p, p//131)

