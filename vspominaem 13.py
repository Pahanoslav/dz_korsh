"""""""""""
a = 4**12 + 2**32 - 16
a = bin(a)[2::]
print(a.count('1'))
"""""""""""
for x in '012345678':
    if ((int('88' + str(x) + '4' + str(x), 9) + int('7' + str(x) + '344', 9)) % 67) == 0:
        print(((int('88' + str(x) + '4' + str(x), 9) + int('7' + str(x) + '344', 9)) / 67))

