print('x y z w')

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                f = (not(y <= (x == w))) and (z <= x)
                if f == 1:
                    print(x, y, z, w)
