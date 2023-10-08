mlg = open('107_17.txt')
sas = mlg.read()
sas = sas.split('\n')
sas = [int(i) for i in sas]
s = []
for i in range(1, len(sas)):
    if sas[i] % 21 == 0:
        s.append(sas[i])
m = min(s)
gg = 0
h = 0

for j in range(len(sas)-1):
    if sas[j] % m == 0  or sas[j+1] % m == 0:
        gg += 1
        h = max(sas[j] + sas[j+1], h)
print(gg, h)



