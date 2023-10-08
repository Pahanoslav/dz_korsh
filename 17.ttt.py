og = open('17_7596.txt').read()
og = og.split('\n')
og = [int(i) for i in og]
minn = 100000000000000
count = 0
c = []
for i in range(len(og)):
    if (og[i] % 10 == 5) and (len(str(og[i]))) == 3 and (og[i] < minn):
        minn = og[i]
for i in range(len(og) - 1):
    if (not((len(str(og[i])) == 3) == (len(str(og[i+1])) == 3))) and ((og[i] + og[i+1]) % minn == 0):
        count += 1
        c.append(og[i] + og[i+1])
print(count, min(c))

