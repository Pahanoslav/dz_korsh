
"""
for x in range(0, 11):
    for y in range(0, 11):
        s1 = 7*25**5+y*25**4+2*25**3+
        s2 = 6*11**4+7*11*3+x*11**2+9*11**1+y\
"""

a1 = "7"
a2 = "23"
a3 = "5"

b1 = "67"
b2 = "9"
b3 = ""
"""
for x in '0123456789A':
    for y in '0123456789A':
        a = a1 + y + a2 + x + a3
        b = b1 + x + b2 + y
        a = int(a, 25)
        b = int(b, 11)
    if (a + b)%131 == 0:
        print((a+b) / 131)
"""

"""
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (f(n-1)-f(n-2))*n
print(f(8))
"""

def f(n):
    if n < 3:
        return 3 * n
    elif n > 2 and n % 2 == 0:
        return f(n-2)*f(n-1)-n
    elif n > 2 and n % 2 != 0:
        return f(n-1)- f(n-2) + 2*n
print(f(30))









