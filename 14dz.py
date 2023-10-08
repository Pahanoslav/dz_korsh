import requests
text = requests.get('https://kpolyakov.spb.ru/cms/files/ege-sym/24-230.txt').text
c = []
for i in range(len(text)-1):
    if (text[i] == 'K' and text[i+1] == 'K' and text[i+2] == '4' and text[i+3] == '3' and text[i+4] in '0123456789' \
        and text[i+5] in '0123456789' and text[i+6] == '7'  and text[i+7] == '8' and text[i+8] in '0123456789' \
        and text[i+9] in '0123456789' and text[i+10] in '0123456789' and text[i+11] == '3' and text[i+12] == '4' \
        and text[i+13] =='K' and text[i+14] == 'K') == True:
        c.append(text[i+2:i+13])



