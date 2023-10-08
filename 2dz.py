a = open('17 (1).txt')
a = a.read()
a = a.split('\n')
a = [int(i) for i in a]
b = 0
mx = -10000000000000
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] * a[j] % 14 != 0:
            b += 1
            c = a[i] + a[j]
            if mx < c:
                mx = c
print(b, mx)




