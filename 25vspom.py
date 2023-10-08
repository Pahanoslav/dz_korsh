# k = 0
# for i in range(10000000, 10000000000):
#     c = []
#     for j in range(1, int(i**(1/2)) + 1):
#         if i % j == 0:
#             c.append(j)
#             if j != 1 and j != i//j:
#                 c.append(i//j)
#     c.sort()
#     if len(c) < 2:
#         pass
#     else:
#         if 0 < (c[-1] + c[-2]) < 10000:
#             k += 1
#
#             print(i, c[-1] + c[-2])
#     if k == 5:
#         break


# for qe in range(0, 10):
#     s = int('1' + str(qe) + '21394')
#     if s % 2023 == 0:
#         print(s, s // 2023)
#
# for qe in range(0, 10):
#     for st in range(0, 10):
#         s = int('1' + str(qe) + '2139' + str(st) + '4')
#         if s % 2023 == 0:
#             print(s, s // 2023)
#
# for qe in range(0, 10):
#     for st in range(0, 10):
#         for st2 in range(0, 10):
#             s = int('1' + str(qe) + '2139' + str(st) + str(st2) + '4')
#             if s % 2023 == 0:
#                 print(s, s // 2023)
#
# for qe in range(0, 10):
#     for st in range(0, 10):
#         for st2 in range(0, 10):
#             for st3 in range(0, 10):
#                 s = int('1' + str(qe) + '2139' + str(st) + str(st2) + str(st3) + '4')
#                 if s % 2023 == 0:
#                     print(s, s // 2023)

for i in range(201455, 201470):
    c = []
    for j in range(1, i+1):
        if i % j == 0:
            c.append(j)
    if len(c) == 4:
        print(i, c)









