text = open('dedan.txt').read()
c = []
s = 0
i = 0
while i < len(text)-2:
    s = 0
    if text[i] + text[i+1] + text[i+2] == 'XYZ':
        i += 3
        s += 3
        while True and i < len(text)-2:
            if text[i] + text[i+1] + text[i+2] == 'XYZ':
                i += 3
                s += 3
            elif text[i] + text[i+1] == 'XY':
                s += 2
                c.append(s)
                break
            elif text[i] == 'X':
                s += 1
                c.append(s)
                break
            else:
                c.append(s)
                break
    i += 1
print(max(c))


