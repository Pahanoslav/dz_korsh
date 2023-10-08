y = []
k = open('ogss.txt').read()
k = k.split('\n')
del k[-1]
k = [int(i) for i in k]

c = []
f = sum(k)/len(k)
counter = 0
for i in range(1, len(k)-2):
    if k[i] * k[i+1] > k[i-1] * k[i+2]:
        c.append(k[i])
        c.append(k[i+1])

for i in range(0, len(c), 2):
    y.append(c[i] + c[i+1])

    if c[i] > f or c[i+1] > f:
        counter += 1
print(max(y), counter)




