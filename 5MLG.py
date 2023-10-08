
for n in range(0, 35):
    s = bin(n)[2::]
    if s.count('1') % 2 == 0:
        s = '10'+s[2::]+'0'
    else:
        s = '11'+s[2::]+'1'
    if int(s, 2) < 35:
        print(n)
