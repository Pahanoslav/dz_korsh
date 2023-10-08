text = open('pahan.txt').read()
dct = {}
for i in range(len(text)):
    if text[i] == "A":
        if text[i+1] in dct:
            dct[text[i+1]] += 1
        else:
            dct[text[i+1]] = 1



print(dct)
