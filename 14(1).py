c = ''
m = 3*625**173+4*125**180+3*25**157+2*5**155+156
count = 0
while m != 0:
    c = m%25
    m = m // 25
    if c == 0:
        count += 1
print(count)



