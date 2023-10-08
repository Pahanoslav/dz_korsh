# def f(x, y, z):
#     if x + y >= 107 and z == 3:
#         return 1
#     elif x + y >= 107 and z < 3:
#         return 0
#     elif x + y < 107 and z == 3:
#         return 0
#     else:
#         return f(x + 1, y, z+1) or f(x * 2, y, z+1) or f(x, y + 1, z+1) or f(x, y * 2, z+1)
#
# for s in range(1, 94):
#     if f(13, s, 1):
#         print(s)


# def f(x, y, z):
#     if x + y >= 107 and z == 4:
#         return 1
#     elif x + y >= 107 and z < 4:
#         return 0
#     elif x + y < 107 and z == 4:
#         return 0
#     else:
#         if z % 2 == 1:
#             return f(x*2, y, z+1) or f(x+1, y, z+1) or f(x, y*2, z+1) or f(x, y+1, z+1)
#         else:
#             return f(x*2, y, z+1) and f(x+1, y, z+1) and f(x, y*2, z+1) and f(x, y+1, z+1)
#
# for s in range(1, 94):
#     if f(13, s, 1):
#         print(s)


# def f(x, y, z):
#     if z == 3 and x + y <= 40:
#         return 1
#     elif z == 3 and x + y > 40:
#         return 0
#     elif z < 3 and x + y <= 40:
#         return 0
#     else:
#         return f(x - 1, y, z+1) or f(x // 2 + x % 2, y, z+1) or f(x, y-1, z+1) or f(x, y//2 + y % 2, z+1)
#
# for s in range(1000, 21, -1):
#     if f(20, s, 1):
#         print(s)

# def f(x, y, z):
#     if z == 4 and x + y <= 40:
#         return 1
#     elif z == 4 and x + y > 40:
#         return 0
#     elif z < 4 and x + y <= 40:
#         return 0
#     else:
#         if z % 2 == 1:
#             return f(x - 1, y, z+1) or f(x // 2 + x % 2, y, z+1) or f(x, y-1, z+1) or f(x, y//2 + y % 2, z+1)
#         else:
#             return f(x - 1, y, z+1) and f(x // 2 + x % 2, y, z+1) and f(x, y-1, z+1) and f(x, y//2 + y % 2, z+1)
# for s in range(1000, 21, -1):
#     if f(20, s, 1):
#         print(s)


# def f(x, y, z):
#     if z == 3 and x + y >= 41:
#         return 1
#     elif z >= 3 and x + y <= 41:
#         return 0
#     elif x < 3 and x + y >= 41:
#         return 0
#     else:
#         return f(x+1, y+2, z+1) or f(x+2, y+2, z+1) or f(x*2, y, z+1) or f(x, y*2, z+1)
# for s in range(1, 32):
#     if f(8, s, 1):
#         print(s)
#
# def f(x, y, z):
#     if z == 4 and x + y >= 41:
#         return 1
#     elif z >= 4 and x + y <= 41:
#         return 0
#     elif z < 4 and x + y >= 41:
#         return 0
#     else:
#         if z % 2 == 1:
#
#             return f(x+1, y+2, z+1) or f(x+2, y+1, z+1) or f(x*2, y, z+1) or f(x, y*2, z+1)
#         else:
#             return f(x+1, y+2, z+1) and f(x+2, y+1, z+1) and f(x*2, y, z+1) and f(x, y*2, z+1)
#
#
# for s in range(1, 33):
#     if f(8, s, 1):
#         print(s)

# def f(x, y ,z):
#     if z == 3 and x + y >= 77:
#         return 1
#     elif z == 3 and x + y < 77:
#         return 0
#     elif z < 3 and x + y > 77:
#         return 0
#     else:
#         return f(x + 1, y, z+1) or f(x, y + 1, z+1) or f(x * 2, y, z + 1) or f(x, y * 2, z +1)
#
# for s in range(1, 69):
#     if f(8, s, 1):
#         print(s)

# def f(x, y ,z):
#     if z == 4 and x + y >= 77:
#         return 1
#     elif z == 4 and x + y < 77:
#         return 0
#     elif z < 4 and x + y > 77:
#         return 0
#     else:
#         if z % 2 == 1:
#             return f(x + 1, y, z+1) or f(x, y + 1, z+1) or f(x * 2, y, z + 1) or f(x, y * 2, z +1)
#         else:
#             return f(x + 1, y, z+1) and f(x, y + 1, z+1) and f(x * 2, y, z + 1) and f(x, y * 2, z +1)
#
# for s in range(1, 69):
#     if f(8, s, 1):
#         print(s)

# def f(x, y ,z):
#     if (z == 3 or z == 5) and x + y >= 77:
#         return 1
#     elif z == 5 and x + y < 77:
#         return 0
#     elif z < 5 and x + y > 77:
#         return 0
#     else:
#         if z % 2 == 0:
#             return f(x + 1, y, z+1) or f(x, y + 1, z+1) or f(x * 2, y, z + 1) or f(x, y * 2, z +1)
#         else:
#             return f(x + 1, y, z+1) and f(x, y + 1, z+1) and f(x * 2, y, z + 1) and f(x, y * 2, z +1)
#
# for s in range(1, 69):
#     if f(8, s, 1):
#         print(s)

# def f(x, y, z):
#     if z == 4 and x + y == 13:
#         return 1
#     elif z == 4 and x + y != 13:
#         return 0
#     elif z != 4 and x + y == 13:
#         return 0
#     elif (z != 4 or z != 2) and x + y == 13:
#         return 1
#     else:
#         if z % 2 == 1:
#             return f(x + 1, y, z + 1) or f(x + 2, y, z + 1) or f(x, y + 1, z + 1) or f(x, y + 2, z + 1)
#         else:
#             return f(x + 1, y, z + 1) and f(x + 2, y, z + 1) and f(x, y + 1, z + 1) and f(x, y + 2, z + 1)
# for s in range(1, 10):
#     if f(3, s, 1):
#         print(s)
#
# def f(x, y ,z):
#     if x + y >= 77 and z == 3:
#         return 1
#     elif x + y >= 77 and z < 3:
#         return 0
#     elif x + y < 77 and z == 3:
#         return 0
#     elif x + y >= 77 and z > 3:
#         return 0
#     else:
#         return f(x + 1, y, z+1) or f(x * 2, y, z+1) or f(x, y + 1, z +1) or f(x, y * 2, z + 1)
# for s in range(1, 70):
#     if f(7, s, 1):
#         print(s)



# def f(x, y ,z):
#     if x + y >= 77 and (z == 5 or z == 3):
#         return 1
#     elif x + y >= 77 and z < 5:
#         return 0
#     elif x + y < 77 and z == 5:
#         return 0
#     elif x + y >= 77 and z > 5:
#         return 0
#     else:
#         if z % 2 == 0:
#
#             return f(x + 1, y, z+1) or f(x * 2, y, z+1) or f(x, y + 1, z +1) or f(x, y * 2, z + 1)
#
#         else:
#              return f(x + 1, y, z+1) and f(x * 2, y, z+1) and f(x, y + 1, z +1) and f(x, y * 2, z + 1)
# for s in range(1, 70):
#     if f(7, s, 1):
#         print(s)

def f(a, n):
    if n == 3 and a <= 10:
        return 1
    elif n < 3 and a <= 10:
        return 0
    elif n == 3 and a > 10:
        return 0
    else:
        return f(a - 10, n + 1) or f(a//3, n + 1)
for s in range(11, 1000):
    if f(s, 1):
        print(s)





























































