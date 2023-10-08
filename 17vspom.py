
""""""""""
a = open('vspom.txt').read()
a = a.split('\n')
del a[-1]
a = [int(i) for i in a]
maxx = -1000000
for i in range(len(a)):
    if a[i] % 10 == '3' and a[i] > maxx:
        maxx = a[i]
nigga = 0
c = []
for i in range(len(a)-1):
    if (not((a[i] % 10 == 3) == (a[i+1] % 10 == 3))) and ((a[i]**2 + a[i+1]**2) >= maxx**2):
        nigga += 1
        c.append(a[i]**2 + a[i+1]**2)
print(nigga, max(c))
"""""""""

a = open('vspom2.txt').read()
a = a.split('\n')
del a[-1]
a = [int(i) for i in a]
nigga = 0
c = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if ((a[i] - a[j]) % 45 == 0) and (a[i] % 18 == 0 or a[j] % 18 == 0):
            nigga += 1
            c.append(a[i] - a[j])
print(nigga, max(c))

