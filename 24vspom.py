# a = open('mlg.txt').read()
# a = a[0:-1]
# a = a.replace('L', ' ')
# a = a.replace('D', ' ')
# a = a.split(' ')
# print(a)
# print(max([len(i) for i in a]))

a = open('caca.txt').read()
dct = {}
for i in range(1, len(a) - 1):
    if a[i-1] == a[i+1]:
        if a[i] in dct:
            dct[a[i]] += 1
        else:
            dct[a[i]] = 1

print(dct)

