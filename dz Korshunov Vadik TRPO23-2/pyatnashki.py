
import random

def correct_test(pol):
    messes = 0
    m = []
    for i in pol:
        for j in i:
            if (j != '  ') and (j != ' '):
                m.append(int(j))
    for i in range(len(m)):
        element = m[i]
        for j in range(i+1, len(m)):
            if m[j] < element:
                messes += 1
    if messes % 2 == 0:
        return True
    else:
        return False
def tegeg(number):
    if len(number) == 1:
            number = ' ' + number
    return number
def test(number, pol):
    g = 0
    for i in range(4):
        for j in range(4):
            if pol[i][j] == number:
                g = 1
                break
        if g == 1:
            break
    if g == 1:
        return True
    else:
        return False


z = input('Нажмите Enter чтобы начать игру!')


pol = [[0, 0, 0, 0] for i in range(4)]
m = ['  ', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13', '14', '15']
result = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13', '14', '15', '  ']
random.shuffle(m)

while not correct_test(m):
    random.shuffle(m)

k = 0
steps = 0

for i in range(4):
    for j in range(4):
        pol[i][j] = m[k]
        k += 1



while True:
    # поле
    print(' __________________________')
    print('')
    print('|  ' + pol[0][0] + '  |  '+ pol[0][1] + '  |  ' + pol[0][2] + '  | ' + pol[0][3] + '  |')
    print(' __________________________')
    print('')
    print('|  ' + pol[1][0] + '  |  '+ pol[1][1] + '  |  ' + pol[1][2] + '  | ' + pol[1][3] + '  |')
    print(' __________________________')
    print('')
    print('|  ' + pol[2][0] + '  |  '+ pol[2][1] + '  |  ' + pol[2][2] + '  | ' + pol[2][3] + '  |')
    print(' __________________________')
    print('')
    print('|  ' + pol[3][0] + '  |  '+ pol[3][1] + '  |  ' + pol[3][2] + '  | ' + pol[3][3] + '  |')
    print(' __________________________')
    print('')
    number = tegeg(input('Введите число, которое хотите переместить на пустое место: '))
    if not (test(number, pol)):
        print('Ошибка! Такого числа нет в колоде. Введите число заново')
        print('')
        continue
    else:
        k = 1
        gtg = 1
        for i in range(4):
            for j in range(4):
                if number == pol[i][j]:
                    if (0 <= i+1 <= 3) and (pol[i+1][j] == '  '):
                        pol[i][j], pol[i+1][j] = pol[i+1][j], pol[i][j]
                        gtg = 0
                        break
                    elif (0 <= i-1 <= 3) and (pol[i-1][j] == '  '):
                        pol[i][j], pol[i-1][j] = pol[i-1][j], pol[i][j]
                        gtg = 0
                        break
                    elif (0 <= j+1 <= 3) and (pol[i][j+1] == '  '):
                        pol[i][j], pol[i][j+1] = pol[i][j+1], pol[i][j]
                        gtg = 0
                        break
                    elif (0 <= j-1 <= 3) and (pol[i][j-1] == '  '):
                        pol[i][j], pol[i][j-1] = pol[i][j-1], pol[i][j]
                        gtg = 0
                        break
                    else:
                        print('Ошибка! Это число не может быть сдвинуто!')
                        print('')
                        k = 0
            if gtg == 0:
                break
        if k == 0:
            continue
        else:
            steps += 1
            tst = 1
            delta = 0
            for i in range(4):
                for j in range(4):
                    if pol[i][j] != result[delta]:
                        tst = 0
                        break
                    delta += 1
                if tst == 0:
                    break
            if tst == 1:
                break

print(' __________________________')
print('')
print('|  ' + pol[0][0] + '  |  '+ pol[0][1] + '  |  ' + pol[0][2] + '  | ' + pol[0][3] + '  |')
print(' __________________________')
print('')
print('|  ' + pol[1][0] + '  |  '+ pol[1][1] + '  |  ' + pol[1][2] + '  | ' + pol[1][3] + '  |')
print(' __________________________')
print('')
print('|  ' + pol[2][0] + '  |  '+ pol[2][1] + '  |  ' + pol[2][2] + '  | ' + pol[2][3] + '  |')
print(' __________________________')
print('')
print('|  ' + pol[3][0] + '  |  '+ pol[3][1] + '  |  ' + pol[3][2] + '  | ' + pol[3][3] + '  |')
print(' __________________________')
print('')
print('')
print('Поздравляем!!! Вы выиграли!')
print('Вы сделали {} шагов'.format(steps))
