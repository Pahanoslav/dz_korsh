import requests
a = requests.get('https://kpolyakov.spb.ru/cms/files/ege-sym/24-221.txt').text

i = 0
c = 0
mx = 0
j = []

h = []
while i < len(a):
    null = 0
    edinica = 0
    if a[i] == '0':
        while a[i] == '0':
            null += 1
        if a[i] == '1':
            edinica += 1






