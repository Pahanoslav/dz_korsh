p1 = 254
p2 = 800

q1 = 410
q2 = 823
c = []
for A1 in range(0, 1000):
    for A2 in range(A1, 1000):
        flag = 1
        for x in range(0, 1000):
            if (((p1 <= x <= p2) and (not(A1 <= x <= A2))) <= (q1 <= x <= q2)) == False:
                flag = 0
        if flag == 1:
            c.append(A2-A1)
print(sorted(c))
