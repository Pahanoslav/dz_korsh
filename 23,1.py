f = open('fff.txt').read()
f = f.split('\n')
del f[-1]
f = [int(i) for i in f]
maxx = -10000

for i in range(len(f)):
    if (f[i] > maxx) and (f[i] % 11 == 0):
        maxx = f[i]
counter = 0
c = []
for i in range(len(f)-1):
    if (f[i] + f[i+1] <= maxx) and ((f[i] % 11 == 0) or (f[i+1] % 11 == 0)):
        counter += 1
        c.append(f[i] + f[i+1])
print(counter, max(c))




