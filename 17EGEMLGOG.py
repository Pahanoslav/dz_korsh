g = open('kaka.txt').read()
g = g.split('\n')
g = [int(i) for i in g]

maxx = -100000000
for i in range(len(g)):
    if (len(str(g[i])) == 2) and g[i] > maxx:
        maxx = g[i]


c = []
count = 0
for i in range(len(g)-1):
    if ((100 <= g[i] < 1000) or (100 <= g[i+1] < 1000)) and ((g[i] + g[i+1]) % maxx == 0):
        count += 1
        c.append(g[i] + g[i+1])

print(count, max(c))





