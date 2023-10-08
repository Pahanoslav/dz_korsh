mlg = open('172.txt')
mlg = mlg.read()
mlg = mlg.split('\n')
del mlg[-1]
mlg = [int(i) for i in mlg]
og = 0
mx = -10000000000
for i in range(len(mlg)):
    for j in range(i+1, len(mlg)):
        if ((mlg[i] + mlg[j]) % 2 != 0) and ((mlg[i] * mlg[j]) % 5 == 0):
            og += 1
            a = mlg[i] + mlg[j]
            if mx < a:
                mx = a
print(og, mx)



