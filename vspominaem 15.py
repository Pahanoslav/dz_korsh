"""""""""
c = []
for a1 in range(0, 100):
    for a2 in range(a1+1, 100):
        flag = 1
        x = -100
        while x < 100:
            x += 0.5
            f = (17 <= x <= 54) <= (((37 <= x <= 83) and (not(a1 <= x <= a2))) <= (not(17 <= x <= 54)))
            if f == False:
                flag = 0
        if flag == 1:
            c.append(a2-a1)
print(min(c))
"""""""""""

for a in range(0, 300):
    flag = 1
    for x in range(0, 300):
        for y in range(0, 300):
            if ((x * y < a) or (x < y) or (x >= 12)) == False:
                flag = 0
    if flag == 1:
        print(a)
