'''''''''
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x+1, y) + f(x+2, y) + f(x*2, y)

print(f(3, 10) * f(10, 12))
'''''''''
'''''''''
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x+1, y) + f(x+2, y) + f(x+4, y)
print(f(1, 8)*f(8, 15))
'''''''''
'''''''''
def f(x, y):
    if x > y or x == 16:
        return 0
    elif x == y:
        return 1
    elif x < y:
        return f(x + 1, y) + f(x * 2, y)
print(f(1, 10) * f(10, 21))
'''''''''''

def f(x, y, z, v, k):
    if x > y:
        return 0
    elif x == y:
        return 1
    elif x < y and (x + z + v) % 11 == 0:
        return f(x + 2, y, x, z) + f(x * 3, y, x, z) + f(x * 4, y, x, z)

print(f(1, 600, 0, 0))




