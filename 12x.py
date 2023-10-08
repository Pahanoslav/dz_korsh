g = open('kaka2.txt').read()
count = 0
c = []
res = ["AAA", "AAB", "AAC", "ABA", "ABB", "ABC", "ACA", ]
for i in range(len(g)-2):
    count += 1
    if (g[i] + g[i+1] + g[i+2]) in res:
        c.append(count)
        count = 0
print(max(c))



