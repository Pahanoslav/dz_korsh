import requests
text = requests.get('https://kpolyakov.spb.ru/cms/files/ege-sym/24-215.txt').text
c = ['A11', 'A12', 'A13', 'A21', 'A22', 'A23', 'A31', 'A32', 'A33', 'B11', 'B12', 'B13', 'B21', 'B22', 'B23', 'B31', 'B32', 'B33', \
'C11', 'C12', 'C13', 'C21', 'C22', 'C23', 'C31', 'C32', 'C33']
i = 0
p = []
while i < len(text)-2:
    s = 0
    if (text[i] + text[i+1] + text[i+2]) in c:
        s += 1
        i += 3
        while True and i < len(text) - 2:
            if (text[i] + text[i+1] + text[i+2]) in c:
                s += 1
                i += 3

            else:
                p.append(s)
                break
    else:
        i += 1
print(max(p))
