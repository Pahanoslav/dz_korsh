c = []
for a in range(0, 1000):
    flag = 1
    for x in range(1, 1000):
        f = ((x % 12==0) <= (not((x % 90) == 0))) or (x + 2*a >= 512)
        if f == False:
            flag = 0
    if flag == 1:
        c.append(a)
print(sorted(c))



