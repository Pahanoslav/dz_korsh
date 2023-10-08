c = 0
def f(n):
    global c
    if n == 11:
        c += 1
    elif n < 11:
        f(n+1)
        f(n+2)
f(1)
print(c)


